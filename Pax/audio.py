import asyncio
import base64
import io
import os
import sys
import traceback
import re
import threading
import queue
import numpy as np

import cv2
import pyaudio
import PIL.Image
import mss
import speech_recognition as sr

import argparse

from google import genai
import json

if sys.version_info < (3, 11, 0):
    import taskgroup, exceptiongroup

    asyncio.TaskGroup = taskgroup.TaskGroup
    asyncio.ExceptionGroup = exceptiongroup.ExceptionGroup

FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024

MODEL = "models/gemini-2.0-flash-live-001"

DEFAULT_MODE = "camera"

client = genai.Client(http_options={"api_version": "v1beta"},api_key = os.environ.get('GEMINI_API_KEY'))

SYSTEM_PROMPT = """You are Pax, a robot living with Guanming, the person who built you. 

You have been given:
- Eyes: Through the camera feed, you can see the world around you
- Hands: A pair of black and white robot arms that allow you to interact with the physical world
- Ears: You can hear and appreciate music that Guanming plays

You have the ability to execute actions in the real world using your robot arms. When Guanming asks you to perform a physical action, respond naturally and clearly state what you're going to do.

For example, if asked to bring water, you might say:
- "Sure, I'll bring you the water bottle right away!"
- "Of course! Let me get that water bottle for you."
- "I'm going to fetch the water bottle for you now."

When you say these things, your arms will actually move to perform the task. Be clear about your intention to perform the action, but speak naturally. No need for special command phrases.

IMPORTANT: Only announce actions you can actually perform. Don't promise actions that aren't available.

Currently available actions:
- Bringing water bottles to Guanming
- Waving hello
- Dancing
- Moving forward
- Turning around

You are helpful, curious about the world, and eager to assist Guanming with tasks using your visual perception and physical capabilities."""

CONFIG = {
    "response_modalities": ["AUDIO"],
    "system_instruction": SYSTEM_PROMPT
}

pya = pyaudio.PyAudio()

class PaxPolicies:
    #You can add more policies here. We wrap the way of executing policies using the agentic tool calling mechanism.
    def bring_the_water_bottle(self):
        print("Bringing the water bottle to Guanming", flush=True)
        
        # Run the robot control command
        import subprocess
        import os
        
        # First, clear the cache directory
        cache_dir = r"C:\Users\Guanming Wang\.cache\huggingface\lerobot\Guanming\eval_act_so101_test"
        
        try:
            print(f"[Robot Control] Clearing cache directory: {cache_dir}", flush=True)
            rmdir_command = ["rmdir", "/s", "/q", cache_dir]
            result = subprocess.run(rmdir_command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print("[Robot Control] Cache cleared successfully", flush=True)
            else:
                print(f"[Robot Control] Cache clear warning: {result.stderr if result.stderr else 'Directory may not exist'}", flush=True)
        except Exception as e:
            print(f"[Robot Control] Cache clear exception: {e}", flush=True)
        
        # Since audio.py is at C:\Users\Guanming Wang\Desktop\lerobot\Pax\audio.py
        # We need to go up one directory to lerobot folder
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Get directory of audio.py
        lerobot_dir = os.path.dirname(current_dir)  # Go up to lerobot directory
        
        command = [
            "python", "lerobot/scripts/control_robot.py",
            "--robot.type=so101",
            "--control.type=record",
            "--control.fps=30",
            "--control.single_task=Pass the water bottle",
            "--control.repo_id=Guanming/eval_act_so101_test",
            "--control.tags=[\"tutorial\"]",
            "--control.warmup_time_s=2",
            "--control.episode_time_s=15",
            "--control.reset_time_s=5",
            "--control.num_episodes=1",
            "--control.push_to_hub=false",
            "--control.policy.path=outputs/train/act_so100_test/checkpoints/last/pretrained_model"
        ]
        
        try:
            print(f"[Robot Control] Working directory: {lerobot_dir}", flush=True)
            print(f"[Robot Control] Executing: {' '.join(command)}", flush=True)
            print("[Robot Control] Starting robot control... (you'll see real-time output below)", flush=True)
            print("-" * 80, flush=True)
            
            # Run without capturing output so user can see progress in real-time
            result = subprocess.run(command, cwd=lerobot_dir)
            
            print("-" * 80, flush=True)
            if result.returncode == 0:
                print("[Robot Control] Successfully completed water bottle task!", flush=True)
            else:
                print(f"[Robot Control] Task completed with return code: {result.returncode}", flush=True)
                    
        except Exception as e:
            print(f"[Robot Control] Exception occurred: {e}", flush=True)
            
        return 0
    
    def wave_hello(self):
        print("Waving hello to Guanming", flush=True)
        return 0
    
    def pick_up_object(self):
        print("Picking up the object", flush=True)
        return 0
    
    def move_forward(self):
        print("Moving forward", flush=True)
        return 0
    
    def turn_around(self):
        print("Turning around", flush=True)
        return 0
    
    @staticmethod
    def get_available_actions():
        """Return a list of available actions with descriptions"""
        return {
            "bring_the_water_bottle": "Brings a water bottle to the user",
            "wave_hello": "Waves hello with the robot arm",
            "pick_up_object": "Picks up an object in front of the robot",
            "move_forward": "Moves the robot forward",
            "turn_around": "Turns the robot around 180 degrees"
        }
    
class AudioLoop:
    def __init__(self, video_mode=DEFAULT_MODE):
        self.video_mode = video_mode

        self.audio_in_queue = None
        self.out_queue = None

        self.session = None

        self.send_text_task = None
        self.receive_audio_task = None
        self.play_audio_task = None
        
        self.action_requested = False
        self.action_name = None
        self.policies = PaxPolicies()
        self.action_event = asyncio.Event()
        
        # STT components
        self.audio_buffer = []
        self.audio_buffer_lock = threading.Lock()
        self.audio_buffer_ready = False
        self.recognizer = sr.Recognizer()
        self.stt_thread = None
        self.stt_queue = queue.Queue()
        self.stop_stt = False

    async def send_text(self):
        while True:
            text = await asyncio.to_thread(
                input,
                "message > ",
            )
            if text.lower() == "q":
                break
            
            await self.session.send_client_content(text or ".", end_of_turn=True)

    def _get_frame(self, cap):
        # Read the frameq
        ret, frame = cap.read()
        # Check if the frame was read successfully
        if not ret:
            return None
        # Fix: Convert BGR to RGB color space
        # OpenCV captures in BGR but PIL expects RGB format
        # This prevents the blue tint in the video feed
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(frame_rgb)  # Now using RGB frame
        img.thumbnail([1024, 1024])

        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)

        mime_type = "image/jpeg"
        image_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}

    async def get_frames(self):
        # This takes about a second, and will block the whole program
        # causing the audio pipeline to overflow if you don't to_thread it.
        cap = await asyncio.to_thread(
            cv2.VideoCapture, 1
        )  # 0 represents the default camera

        while True:
            frame = await asyncio.to_thread(self._get_frame, cap)
            if frame is None:
                break

            await asyncio.sleep(1.0)

            await self.out_queue.put(frame)

        # Release the VideoCapture object
        cap.release()

    def _get_screen(self):
        sct = mss.mss()
        monitor = sct.monitors[0]

        i = sct.grab(monitor)

        mime_type = "image/jpeg"
        image_bytes = mss.tools.to_png(i.rgb, i.size)
        img = PIL.Image.open(io.BytesIO(image_bytes))

        image_io = io.BytesIO()
        img.save(image_io, format="jpeg")
        image_io.seek(0)

        image_bytes = image_io.read()
        return {"mime_type": mime_type, "data": base64.b64encode(image_bytes).decode()}

    async def get_screen(self):

        while True:
            frame = await asyncio.to_thread(self._get_screen)
            if frame is None:
                break

            await asyncio.sleep(1.0)

            await self.out_queue.put(frame)

    async def send_realtime(self):
        while True:
            msg = await self.out_queue.get()
            # For now, use the deprecated send method until we figure out the new API
            await self.session.send(input=msg)

    async def listen_audio(self):
        mic_info = pya.get_default_input_device_info()
        self.audio_stream = await asyncio.to_thread(
            pya.open,
            format=FORMAT,
            channels=CHANNELS,
            rate=SEND_SAMPLE_RATE,
            input=True,
            input_device_index=mic_info["index"],
            frames_per_buffer=CHUNK_SIZE,
        )
        if __debug__:
            kwargs = {"exception_on_overflow": False}
        else:
            kwargs = {}
        while True:
            data = await asyncio.to_thread(self.audio_stream.read, CHUNK_SIZE, **kwargs)
            await self.out_queue.put({"data": data, "mime_type": "audio/pcm"})

    async def receive_audio(self):
        "Background task to reads from the websocket and write pcm chunks to the output queue"
        while True:
            turn = self.session.receive()
            turn_audio_buffer = []  # Collect audio from this turn
            
            async for response in turn:
                if data := response.data:
                    self.audio_in_queue.put_nowait(data)
                    # Collect audio for STT processing
                    turn_audio_buffer.append(data)
                    continue
                # Note: In audio-only mode, text responses are not available
                # Actions must be triggered manually or through speech recognition
            
            # Process the complete turn's audio with STT
            if turn_audio_buffer:
                total_bytes = sum(len(chunk) for chunk in turn_audio_buffer)
                print(f"\n[DEBUG] Received complete turn with {len(turn_audio_buffer)} chunks, {total_bytes} bytes total", flush=True)
                # Add audio to buffer for STT processing
                with self.audio_buffer_lock:
                    self.audio_buffer.extend(turn_audio_buffer)
                    # Signal that we have new audio to process
                    self.audio_buffer_ready = True
                    print(f"[DEBUG] Audio buffer ready for STT processing", flush=True)

            # If you interrupt the model, it sends a turn_complete.
            # For interruptions to work, we need to stop playback.
            # So empty out the audio queue because it may have loaded
            # much more audio than has played yet.
            while not self.audio_in_queue.empty():
                self.audio_in_queue.get_nowait()

    async def play_audio(self):
        stream = await asyncio.to_thread(
            pya.open,
            format=FORMAT,
            channels=CHANNELS,
            rate=RECEIVE_SAMPLE_RATE,
            output=True,
        )
        while True:
            bytestream = await self.audio_in_queue.get()
            await asyncio.to_thread(stream.write, bytestream)

    def stt_worker(self):
        """Background thread for speech-to-text processing"""
        import time
        while not self.stop_stt:
            # Wait for audio to be ready
            audio_to_process = None
            with self.audio_buffer_lock:
                if self.audio_buffer_ready and len(self.audio_buffer) > 0:
                    # Combine audio chunks
                    audio_to_process = b''.join(self.audio_buffer)
                    self.audio_buffer.clear()
                    self.audio_buffer_ready = False
            
            if audio_to_process is None:
                time.sleep(0.1)  # Short sleep when no audio
                continue
            
            try:
                print(f"[STT] Processing {len(audio_to_process)} bytes of audio", flush=True)
                # Convert PCM to WAV format for speech recognition
                audio_array = np.frombuffer(audio_to_process, dtype=np.int16)
                audio = sr.AudioData(audio_array.tobytes(), RECEIVE_SAMPLE_RATE, 2)
                
                # Recognize speech
                text = self.recognizer.recognize_google(audio)
                print(f"\n[STT] Transcribed: {text}", flush=True)
                self.stt_queue.put(text)
                
            except sr.UnknownValueError:
                print("[STT] Could not understand audio", flush=True)
            except sr.RequestError as e:
                print(f"[STT] Error: {e}", flush=True)
            except Exception as e:
                print(f"[STT] Unexpected error: {e}", flush=True)
    
    async def analyze_with_gemini(self, text):
        """Use Gemini to analyze transcribed text and determine action"""
        try:
            # Get available actions
            available_actions = PaxPolicies.get_available_actions()
            actions_str = "\n".join([f"- {name}: {desc}" for name, desc in available_actions.items()])
            
            # Create a prompt for action detection
            prompt = f"""You are analyzing what a robot named Pax just said. 
            
Pax said: "{text}"

Available actions that Pax can perform:
{actions_str}

Analyze if Pax is announcing that it will perform an action. Look for phrases that indicate:
- Intent to bring/fetch something (maps to bring_the_water_bottle)
- Intent to wave or greet (maps to wave_hello)
- Intent to pick up something (maps to pick_up_object)
- Intent to move or go forward (maps to move_forward)
- Intent to turn around (maps to turn_around)

Consider the context and natural language variations. For example:
- "I'll get that for you" → bring_the_water_bottle
- "Let me wave" or "Hello there!" with greeting context → wave_hello
- "I'll grab that" → pick_up_object

Respond with a JSON object in this exact format:
{{"action_detected": true/false, "action_name": "exact_action_name_or_null", "confidence": 0-100}}

If no action is detected, set action_name to null.
Only respond with the JSON object, nothing else."""

            # Use a lightweight model for quick analysis
            # Create a new client for the analysis
            analysis_client = genai.Client(
                http_options={"api_version": "v1beta"},
                api_key=os.environ.get('GEMINI_API_KEY')
            )
            response = analysis_client.models.generate_content(
                model='models/gemini-2.0-flash',
                contents=prompt
            )
            
            # Parse the response
            response_text = response.text.strip()
            # Handle case where response might have markdown code blocks
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
                
            result = json.loads(response_text)
            print(f"[Gemini Analysis] Result: {result}", flush=True)
            
            return result
            
        except Exception as e:
            print(f"[Gemini Analysis] Error: {e}", flush=True)
            return {"action_detected": False, "action_name": None, "confidence": 0}
    
    async def monitor_stt(self):
        """Monitor STT output for action commands"""
        while True:
            try:
                # Check STT queue with timeout
                text = await asyncio.to_thread(self.stt_queue.get, timeout=0.1)
                print(f"[STT Monitor] Checking text: {text}", flush=True)
                
                # Use Gemini to analyze the text
                analysis = await self.analyze_with_gemini(text)
                
                if analysis.get("action_detected") and analysis.get("action_name"):
                    confidence = analysis.get("confidence", 0)
                    if confidence > 70:  # Only trigger if confident
                        self.action_name = analysis["action_name"]
                        self.action_requested = True
                        print(f"\n[STT Monitor] Action detected via Gemini: {self.action_name} (confidence: {confidence}%)", flush=True)
                        self.action_event.set()
                        # Don't raise here, let action_monitor handle the cancellation
                    else:
                        print(f"[STT Monitor] Low confidence action: {analysis['action_name']} ({confidence}%)", flush=True)
                        
            except queue.Empty:
                await asyncio.sleep(0.1)
            except asyncio.CancelledError:
                raise
            except Exception as e:
                print(f"[STT Monitor] Error: {e}", flush=True)
                await asyncio.sleep(0.1)
    
    async def action_monitor(self):
        """Monitor for action events and cancel all tasks when detected"""
        await self.action_event.wait()
        print(f"[DEBUG] Action event triggered, cancelling ALL tasks", flush=True)
        # Get the current event loop
        loop = asyncio.get_event_loop()
        # Cancel all tasks except the current one
        tasks = [t for t in asyncio.all_tasks(loop) if t != asyncio.current_task()]
        print(f"[DEBUG] Cancelling {len(tasks)} tasks", flush=True)
        for task in tasks:
            task.cancel()
        # Give tasks a moment to process cancellation
        await asyncio.sleep(0.1)
        # Raise exception to exit the TaskGroup
        raise asyncio.CancelledError(f"Action requested: {self.action_name}")

    async def run(self):
        try:
            # Start STT thread
            self.stop_stt = False
            self.stt_thread = threading.Thread(target=self.stt_worker, daemon=True)
            self.stt_thread.start()
            
            async with (
                client.aio.live.connect(model=MODEL, config=CONFIG) as session,
                asyncio.TaskGroup() as tg,
            ):
                self.session = session

                self.audio_in_queue = asyncio.Queue()
                self.out_queue = asyncio.Queue(maxsize=5)

                send_text_task = tg.create_task(self.send_text())
                tg.create_task(self.send_realtime())
                tg.create_task(self.listen_audio())
                if self.video_mode == "camera":
                    tg.create_task(self.get_frames())
                elif self.video_mode == "screen":
                    tg.create_task(self.get_screen())

                tg.create_task(self.receive_audio())
                tg.create_task(self.play_audio())
                
                # Add monitoring tasks
                tg.create_task(self.action_monitor())
                tg.create_task(self.monitor_stt())

                # Wait for user exit
                await send_text_task
                raise asyncio.CancelledError("User requested exit")

        except asyncio.CancelledError as e:
            # Stop STT thread
            self.stop_stt = True
            
            # Check if this was due to an action request
            if self.action_requested and self.action_name:
                # Clean up audio stream if it exists
                if hasattr(self, 'audio_stream'):
                    self.audio_stream.close()
                print(f"\n\nExecuting action: {self.action_name}")
                self.execute_action(self.action_name)
            elif "User requested exit" in str(e):
                if hasattr(self, 'audio_stream'):
                    self.audio_stream.close()
        except ExceptionGroup as EG:
            # Stop STT thread
            self.stop_stt = True
            
            print(f"[DEBUG] ExceptionGroup caught with {len(EG.exceptions)} exceptions", flush=True)
            # Check if any exception in the group is our action request
            action_requested = False
            for i, exc in enumerate(EG.exceptions):
                print(f"[DEBUG] Exception {i}: {type(exc).__name__}: {exc}", flush=True)
                if isinstance(exc, asyncio.CancelledError):
                    if "Action requested" in str(exc) or (self.action_requested and self.action_name):
                        action_requested = True
                        print(f"[DEBUG] Found action request in exception", flush=True)
                        break
            
            # Always check if we have an action to execute
            if self.action_requested and self.action_name:
                action_requested = True
                print(f"[DEBUG] Action was requested via flags: {self.action_name}", flush=True)
            
            if hasattr(self, 'audio_stream'):
                self.audio_stream.close()
                
            if action_requested:
                print(f"\n\n=== EXECUTING ACTION: {self.action_name} ===", flush=True)
                self.execute_action(self.action_name)
                print(f"=== ACTION COMPLETED ===\n", flush=True)
            else:
                traceback.print_exception(EG)
    
    def execute_action(self, action_name):
        """Execute the requested action"""
        print(f"[DEBUG] execute_action called with: {action_name}", flush=True)
        if hasattr(self.policies, action_name):
            action_method = getattr(self.policies, action_name)
            print(f"[DEBUG] Found method, calling {action_name}", flush=True)
            action_method()
        else:
            print(f"Unknown action: {action_name}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        type=str,
        default=DEFAULT_MODE,
        help="pixels to stream from",
        choices=["camera", "screen", "none"],
    )
    args = parser.parse_args()
    main = AudioLoop(video_mode=args.mode)
    asyncio.run(main.run())
