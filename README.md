<h1 align="center">Fullstack Embodied AI Guide</h1>
<div align="center">
  <img width="300" alt="f939a2605d4f7fcccc692090e379753" src="https://github.com/user-attachments/assets/6145c4a7-bf46-4650-b57c-e90c18fe220e" />
</div>

## **Ready to launch into robotics?** 🤖🚀

This guide is your **ultimate starting point** for bringing **embodied AI** to **life**🏠\! We'll walk you through everything: **building your robot** from scratch to **training a robotic model** and equipping it with **cutting-edge AI control techniques** like **Diffusion Policy**, **ACT**, **Visual-Language Model(VLM) like smolVLM** and **Visual-Language-Action Model(VLA) like pi0.** 🧠✨

Whether you're a beginner curious about robots or eager to explore advanced AI, get ready for a **hands-on learning adventure** that makes complex concepts **simple and fun\!** 🌟🛠️

By the end of this guide, you will be able to **Create Your Own Robotic Agent!** You can also [**Say hi to Pax**](https://www.linkedin.com/feed/update/urn:li:activity:7347260255132676097/) to see an example of what's possible! 

---
<div class="flex flex-col lg:flex-row gap-4 p-4 lg:p-8 bg-gray-100 rounded-lg shadow-inner">
  <div class="w-full lg:w-1/2 bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
    <h3 class="text-2xl font-bold mb-4 text-center text-gray-800 dark:text-white">1. Hardware</h3>
    <ul class="list-none space-y-2 text-gray-700 dark:text-gray-200">
      <li>1.1 <a href="#getting-started-acquiring-your-so-arm101" class="text-blue-600 hover:underline">Getting Started: Acquiring Your SO-ARM101</a>
        <ul class="ml-4 list-disc list-inside space-y-1">
          <li><a href="#build-your-own" class="text-blue-600 hover:underline">Build Your Own</a></li>
          <li><a href="#purchase-a-kit" class="text-blue-600 hover:underline">Purchase a Kit</a></li>
        </ul>
      </li>
      <li>1.2 <a href="#setting-up-your-robotic-arm" class="text-blue-600 hover:underline">Setting Up Your Robotic Arm</a>
        <ul class="ml-4 list-disc list-inside space-y-1">
          <li><a href="#setting-up-your-robotic-arm" class="text-blue-600 hover:underline">Download the Servo Configuration Tool</a></li>
          <li><a href="#setting-up-your-robotic-arm" class="text-blue-600 hover:underline">Follow the Configuration Tutorial</a></li>
          <li><a href="#setting-up-your-leaderfollower-arm-servos" class="text-blue-600 hover:underline">Setting Up Your Leader&Follower Arm Servos</a></li>
        </ul>
      </li>
      <li>1.3 <a href="#assembling-and-wiring-your-robotic-arm" class="text-blue-600 hover:underline">Assembling and Wiring Your Robotic Arm</a>
        <ul class="ml-4 list-disc list-inside space-y-1">
          <li><a href="#assembling-and-wiring-your-robotic-arm" class="text-blue-600 hover:underline">Assembly CAD Animation</a></li>
          <li><a href="#assembling-and-wiring-your-robotic-arm" class="text-blue-600 hover:underline">Assembly Real Demonstration</a></li>
          <li><a href="#assembling-and-wiring-your-robotic-arm" class="text-blue-600 hover:underline">Wiring Demonstration</a></li>
        </ul>
      </li>
      <li>1.4 <a href="#joint-midpoint-and-limit-settings" class="text-blue-600 hover:underline">Joint Midpoint and Limit Settings</a></li>
      <li>1.5 <a href="#joint-calibration" class="text-blue-600 hover:underline">Joint Calibration</a></li>
      <li>1.6 <a href="#teleoperation" class="text-blue-600 hover:underline">Teleoperation</a></li>
      <li>1.7 <a href="#camera-setup" class="text-blue-600 hover:underline">Camera Setup</a>
        <ul class="ml-4 list-disc list-inside space-y-1">
          <li><a href="#gripper-camera-mount" class="text-blue-600 hover:underline">Gripper Camera Mount</a></li>
          <li><a href="#fixed-environment-camera" class="text-blue-600 hover:underline">Fixed Environment Camera</a></li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="w-full lg:w-1/2 bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6">
    <h3 class="text-2xl font-bold mb-4 text-center text-gray-800 dark:text-white">2. Software</h3>
    <ul class="list-none space-y-2 text-gray-700 dark:text-gray-200">
      <li>2.1 <a href="#camera-configuration-and-data-recording" class="text-blue-600 hover:underline">Camera Configuration and Data Recording</a>
        <ul class="ml-4 list-disc list-inside space-y-1">
          <li><a href="#identifying-camera-ids" class="text-blue-600 hover:underline">Identifying Camera IDs</a></li>
          <li><a href="#camera-resolution-and-fov" class="text-blue-600 hover:underline">Camera Resolution and FOV</a></li>
          <li><a href="#camera-encoding-stream-settings" class="text-blue-600 hover:underline">Camera Encoding Stream Settings</a></li>
          <li><a href="#local-recording" class="text-blue-600 hover:underline">Local Recording</a></li>
        </ul>
      </li>
      <li>2.2 <a href="#training-configuration" class="text-blue-600 hover:underline">Training Configuration</a></li>
      <li>2.3 <a href="#real-time-inference-test" class="text-blue-600 hover:underline">Real-Time Inference Test</a>
        <ul class="ml-4 list-disc list-inside space-y-1">
          <li><a href="#running-the-inference-test" class="text-blue-600 hover:underline">Running the Inference Test</a></li>
          <li><a href="#common-issues-during-inference" class="text-blue-600 hover:underline">Common Issues During Inference</a></li>
        </ul>
      </li>
      <li><a href="#environment-setup" class="text-blue-600 hover:underline">Environment Setup</a>
        <ul class="ml-4 list-disc list-inside space-y-1">
          <li><a href="#installing-miniconda" class="text-blue-600 hover:underline">Installing Miniconda (Recommended Python 3.10)</a></li>
          <li><a href="#creating-a-virtual-environment" class="text-blue-600 hover:underline">Creating a Virtual Environment</a></li>
          <li><a href="#cloning-the-code-repository" class="text-blue-600 hover:underline">Cloning the Code Repository</a></li>
          <li><a href="#installing-dependencies" class="text-blue-600 hover:underline">Installing Dependencies</a></li>
          <li><a href="#installing-ffmpeg" class="text-blue-600 hover:underline">Installing FFmpeg</a></li>
        </ul>
      </li>
    </ul>
  </div>
</div>

---

### **Environment Setup**

This section guides you through configuring your environment, including installing Miniconda, creating a virtual environment, and cloning the required code repositories.

#### Installing Miniconda (Recommended Python 3.10)

Miniconda is recommended for managing your Python environment.

  * **For Linux:**
    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    sh Miniconda3-latest-Linux-x86_64.sh
    source ~/.bashrc
    ```
  * **For Windows:**
      * You can download the installer from the [official website](https://www.anaconda.com/download/).
      * Alternatively, you can use a previously downloaded version, such as 24.9.2.

#### Creating a Virtual Environment

Use Conda to create and activate a new virtual environment for this project.

```bash
conda create -n lerobot python=3.10
conda activate lerobot
```

*To re-enter the environment later, you only need to run:* `conda activate lerobot`

#### Cloning the Code Repository

```bash
git clone https://github.com/william-Dic/Fullstack-Embodied-AI-Guide.git
cd Fullstack-Embodied-AI-Guide
```

If you wish to experiment with the latest features from the official repository, you can clone it instead:
```bash
git clone https://github.com/huggingface/lerobot.git`
cd lerobot
git checkout aa8f5936
```

#### Installing Dependencies

Navigate into the `lerobot` directory and install the required dependencies, including the drivers for the Feetech servos.

```bash
cd lerobot
pip install -e ".[feetech]"
```

#### Installing FFmpeg

It is recommended to install FFmpeg version 7.1.1, which supports `libsvtav1` encoding.

```bash
conda install -c conda-forge ffmpeg=7.1.1
```


---
## 1. Hardware

### 1.1 Getting Started: Acquiring Your SO-ARM101
<p align="center">
  <img src="https://github.com/user-attachments/assets/f6f5992b-b02d-47b0-93b9-468cc09bba3a" width="400px" style="display: inline-block; margin: 0 10px;">
  <img src="https://github.com/user-attachments/assets/06e1a231-ca57-4cd7-82fa-a757346b884e" width="400px" style="display: inline-block; margin: 0 10px;">
</p>

### Build Your Own

For the DIY enthusiast, you can construct your own SO-ARM101. The official GitHub repository for the **SO-ARM100** (which forms the core design of the 101) provides comprehensive **build instructions** and a detailed **component list**.

* **GitHub Repository:** [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100)

### Purchase a Kit

Prefer to buy a kit? Several retailers offer various options for both the SO-100 and SO-101.

* **PartaBot** (:us: US):
    * Visit: [partabot.com](https://partabot.com)
    * Offers **assembled versions** and also sells LeKiwi and Koch robots.

* **Seeed Studio** (:earth_africa: International / :cn: China):
    * International: [seeedstudio.com/SO-ARM100-Low-Cost-AI-Arm-Kit.html](https://www.seeedstudio.com/SO-ARM100-Low-Cost-AI-Arm-Kit.html)
    * China (Taobao): [item.taobao.com/item.htm?id=878010637397&skuId=5915703371829&spm=a213gs.v2success.0.0.4cbf4831mkqWLn](https://item.taobao.com/item.htm?id=878010637397&skuId=5915703371829&spm=a213gs.v2success.0.0.4cbf4831mkqWLn)
    * Aliexpress: [aliexpress.com/item/3256808696884714.html](https://www.aliexpress.com/item/3256808696884714.html?gatewayAdapt=4itemAdapt)
    * These options typically include **3D printed kits**.

* **WowRobo** (:earth_africa: International / :cn: China):
    * International: [shop.wowrobo.com/products/so-arm101-diy-kit-assembled-version-1](https://shop.wowrobo.com/products/so-arm101-diy-kit-assembled-version-1)
    * China (Taobao): [item.taobao.com/item.htm?ft=t&id=860171734711](https://item.taobao.com/item.htm?ft=t&id=860171734711)
    * They offer **assembled versions**.
---


### 1.2 Setting Up Your Robotic Arm

Once you have your SO-ARM101 kit and components ready, let's dive into the exciting world of robotic arm control! Properly setting up your servo motors is a crucial first step for stable and reliable arm operation. You can also **Follow the Configuration Tutorial**: [LeRobot SO-ARM101 Robotic Arm - Assembly and Setup Guide](https://www.youtube.com/watch?v=70GuJf2jbYk)

* **Download the Servo Configuration Tool:** You'll need the `FD1.9.8.5` servo debugging tool [Download FD1.9.8.5 (250425).zip](https://gitee.com/ftservo/fddebug/blob/master/FD1.9.8.5\(250425\).zip) to configure your servo IDs and parameters.
  <p align="center">
  <img src="https://github.com/user-attachments/assets/c2102d50-6846-43e8-a11e-6e051fc7278d" width="400">
  </p>

* **Setting Up Your Leader&Follower Arm Servos** To ensure your Leader Arm operates correctly, you'll need to match each servo to its specific joint and configure its settings. Different gear ratios mean different torque, so **each servo needs a unique ID corresponding to the joint it will control**.
  <p align="center">
  <img src="https://github.com/user-attachments/assets/4c9a3a68-dac4-4652-813a-a1c6960e2581" width="400px" height="250px" style="display: inline-block; margin: 0 10px;">
  <img src="https://github.com/user-attachments/assets/93bae1dc-88f3-493a-81da-a8cc86f253dd" width="400px" height="250px" style="display: inline-block; margin: 0 10px;">
  </p>

    1.  **Label Your Servos:** Before you begin, I highly recommend **labeling your servos with their intended joint ID (e.g., 1, 2, 3, etc.) on paper**. This will prevent confusion and ensure you connect the right servo to the right place.
    2.  **Configure Servo IDs and Amax:** Once your servos are labeled, you'll use the **Servo Configuration Tool** to set their IDs and Amax values.
        Using the Servo Configuration Tool, you'll need to make two key changes for each servo:
        1.  **Set the Servo ID:** Assign the **corresponding joint ID** that you determined in the labeling step. This ensures the arm's control system can properly communicate with each servo.
        2.  **Adjust Amax to 254:** Always change the **Amax value to 254**. This setting is crucial for optimal performance of your Leader Arm.
        By following these steps, you'll successfully prepare your servos for integration into the Leader Arm, ensuring smooth and accurate movement.

### 1.3 Assembling and Wiring Your Robotic Arm

Now that all your servos are configured, it's time to assemble your robot arm! Please follow the CAD animation and real demonstration videos provided below. **Pay close attention as the CAD for the Leader and Follower arms are different.**

* **Assembly CAD Animation:** [LeRobot SO-ARM101 Robotic Arm Assembly CAD Animation](https://www.bilibili.com/video/BV18gG1z4EZu/?spm_id_from=333.337.search-card.all.click&vd_source=3a694e50ce8cc42bb59f208d9a0785e9)
* **Assembly Real Demonstration:**
    * **Leader Arm Assembly:** [LeRobot SO-ARM101 Leader Arm Assembly](http://www.youtube.com/watch?v=70GuJf2jbYk)
    * **Follower Arm Assembly:** [LeRobot SO-ARM101 Follower Arm Assembly](http://www.youtube.com/watch?v=70GuJf2jbYk&t=24m40s)
* **Wiring Demonstration:** [LeRobot SO-ARM101 Wiring Demenstration](http://www.youtube.com/watch?v=70GuJf2jbYk&t=41m15s)

### 1.4 Joint Midpoint and Limit Settings

To protect your servos and ensure accurate calibration, you need to configure the joint midpoint and limit settings for each servo. After correctly connecting all servos, the FD1.9.8.5 tool should display a screen similar to the one below, with your 6 servos listed on the left.

<p align="center">
<img width="500" alt="73ab90affda9715a740352f5acd9868" src="https://github.com/user-attachments/assets/81eb55c3-a764-4348-a965-c2697e4da608" />
</p>

To set the limits:

1.  Move each joint to its maximum and minimum positions.
2.  Note the *current position* values displayed in the FD1.9.8.5 tool.
3.  Adjust the limit settings for each joint, using the noted values.

* **Joints 1-5:** Leave a margin of 20-30 from the maximum reachable encoder value (address56).
* **Joint 6:** Leave a margin of 10-20 from the maximum reachable encoder value.

For a detailed demonstration, please refer to this video: [LeRobot SO-ARM101 Joint Midpoint and Limit Settings](http://www.youtube.com/watch?v=70GuJf2jbYk&t=54m07s)

---

### **1.5 Joint Calibration**

After setting up your servo limits, the next crucial step is to manually calibrate your **Follower** arm. This process aligns the robot's physical position with its software coordinates, which is essential for accurate movement. **Precise calibration is critical—an inaccurate calibration can damage your motors.**

#### Manually Calibrating the Follower Arm

Once you have both arms connected to power and a USB signal line, run the calibration script below. After running the command, position the Follower arm in the following sequence.

**Important:** The accuracy of your physical poses directly impacts the calibration results. Pay close attention to the following details:

  * For the **"Rotated position,"** the gripper should be completely open and rotated to the right.
  * All other angles should be either parallel or at a 90-degree angle.

**Calibration Sequence:**

<table>
  <tr>
    <td align="center">1. Middle Position</td>
    <td align="center">2. Zero Position</td>
    <td align="center">3. Rotated Position</td>
    <td align="center">4. Rest Position</td>
  </tr>
  <tr>
    <td align="center"><img width="256" height="256" alt="Middle Position" src="https://github.com/user-attachments/assets/95f1327a-2a49-47cd-9f99-bf6010924553" /></td>
    <td align="center"><img width="256" height="256" alt="Zero Position" src="https://github.com/user-attachments/assets/98e2d24a-9f30-4c49-bc57-66779eb21b94" /></td>
    <td align="center"><img width="256" height="256" alt="Rotated Position" src="https://github.com/user-attachments/assets/3c6235e1-3fac-417e-ad5b-b7a5f4ed0c3a" /></td>
    <td align="center"><img width="256" height="256" alt="Rest Position" src="https://github.com/user-attachments/assets/b4d399fd-db0b-418c-a111-440adea07a4f" /></td>
  </tr>
</table>

#### Launching the Calibration Script

  * **For Linux/macOS:**

    ```bash
    python lerobot/scripts/control_robot.py --robot.type=so101 --robot.cameras='{}' --control.type=calibrate --control.arms='["main_follower"]'
    ```

  * **For Windows:**

    ```bash
    python lerobot\scripts\control_robot.py --robot.type=so101 --robot.cameras='{}' --control.type=calibrate --control.arms='[\"main_follower\"]'
    ```

---


### **Manually Calibrating the Leader Arm**

After ensuring both arms are connected to power and the USB signal cable, run the following script to calibrate the poses in order.

**Important:** The accuracy of your physical poses directly impacts the calibration results. Pay close attention to the following details:

  * For the **"Rotated position,"** the gripper should be completely open and rotated to the right.
  * All other angles should be either parallel or at a 90-degree angle.

**Calibration Sequence:**

<table>
  <tr>
    <td align="center">1. Middle Position</td>
    <td align="center">2. Zero Position</td>
    <td align="center">3. Rotated Position</td>
    <td align="center">4. Rest Position</td>
  </tr>
  <tr>
    <td align="center"><img width="256" height="256" alt="Middle Position" src="https://github.com/user-attachments/assets/cd43cd58-e8a2-4f94-bd07-3a6ca005c1fd" /></td>
    <td align="center"><img width="256" height="256" alt="Zero Position" src="https://github.com/user-attachments/assets/89f2d3bb-1289-4510-931b-e5a16bdbaeae" /></td>
    <td align="center"><img width="256" height="256" alt="Rotated Position" src="https://github.com/user-attachments/assets/ae2b2338-909b-43bf-8726-ac7de6cdec93" /></td>
    <td align="center"><img width="256" height="256" alt="Rest Position" src="https://github.com/user-attachments/assets/e7ff33e4-0591-491a-a80d-897ba511c388" /></td>
  </tr>
</table>


#### Launching the Calibration Script

  * **For Linux/macOS:**

    ```bash
    python lerobot/scripts/control_robot.py --robot.type=so101 --robot.cameras='{}' --control.type=calibrate --control.arms='["main_leader"]'
    ```

  * **For Windows:**

    ```bash
    python lerobot\scripts\control_robot.py --robot.type=so101 --robot.cameras='{}' --control.type=calibrate --control.arms='[\"main_leader\"]'
    ```
    
-----

### **1.6 Teleoperation**

#### Calibration Check Before Teleoperation

Before starting teleoperation, it is crucial to check that your calibration is accurate, especially if this is your first time assembling the robot.

  * **Synchronization Check:** Verify if joints \#2, \#3, and \#6 are synchronized with the Leader arm when in the `rest` position. If there is a significant difference, the Follower arm may still have high torque, causing the servo motors to heat up and overheat.
  * **Directional Check:** Additionally, check that each joint of the Follower arm follows correctly when the Leader arm's joints move within their maximum and minimum ranges. If you find that the movement directions are opposite, it means the pose during calibration was inaccurate, and a recalibration is required.
  * **Safety Warning:** If the Leader and Follower arms move in opposite directions and cause a joint to jam, immediately unplug the power to that robotic arm to prevent the motor from burning out.

#### Official Teleoperation Teaching

Before performing a teleoperation session, please ensure that both arms have a consistent pose, preferably in the `rest` position, to avoid sudden, large movements that could cause damage.

To begin, run the following command:

```bash
python lerobot/scripts/control_robot.py --robot.type=so101 --robot.cameras='{}' --control.type=teleoperate
```

When you see a log similar to the one below, it indicates that the status of the Leader and Follower arms has been successfully acquired. You can now move the Leader arm to synchronously control the Follower arm.

```
INFO 2025-05-09 21:16:01 rol_utils.py:82 dt: 3.38 (296.0hz) dtRlead: 1.45 (690.7hz) dtWfoll: 0.32 (3097.9hz) dtRfoll: 1.59 (630.6hz)
INFO 2025-05-09 21:16:01 rol_utils.py:82 dt: 3.23 (309.6hz) dtRlead: 1.49 (670.5hz) dtWfoll: 0.16 (6447.5hz) dtRfoll: 1.56 (639.5hz)
INFO 2025-05-09 21:16:01 rol_utils.py:82 dt: 3.17 (315.7hz) dtRlead: 1.41 (710.3hz) dtWfoll: 0.22 (4470.3hz) dtRfoll: 1.52 (658.8hz)
INFO 2025-05-09 21:16:01 rol_utils.py:82 dt: 3.32 (301.2hz) dtRlead: 1.49 (670.5hz) dtWfoll: 0.26 (3825.6hz) dtRfoll: 1.55 (645.8hz)
INFO 2025-05-09 21:16:01 rol_utils.py:82 dt: 3.66 (273.2hz) dtRlead: 1.72 (580.8hz) dtWfoll: 0.36 (2770.1hz) dtRfoll: 1.55 (644.3hz)
```

**Note:** Due to the presence of the Leader arm's handle, the Follower arm may suddenly raise its head at the beginning when starting from the `rest` position.

#### Troubleshooting

**If you encounter the following error message:**

```
Missing calibration file ".cache/calibration/so101/main_follower.json"
```

This indicates that the calibration was not successful, or you have not placed the calibration file for the assembled product in the correct location. For users who purchased an assembled product, do not press the Enter key, as this will reset the robot arm's center position and invalidate the factory calibration parameters.

---

### **1.7 Camera Setup**

Note: The camera setup is crucial for model performance. Your setup should ideally include a hand-eye camera (mounted on the gripper) and a fixed environment camera. If you only have one camera, the outcome of the model may not be as good.

#### Gripper Camera Mount

<table>
  <tr>
    <td>
      1. <b>Align the Mount:</b> Align the two screw holes on the camera mount with the corresponding holes on the fixed gripper jaw. (Remember to have the M3 nuts pre-embedded inside the fixed gripper jaw during assembly.)
    </td>
    <td align="center">
      <img width="450" alt="Align the Mount" src="https://github.com/user-attachments/assets/edd0a0aa-dfe7-4dbb-96ae-3cdf318fc1cb" />
    </td>
  </tr>
  <tr>
    <td>
      2. <b>Secure the Mount:</b> Once aligned, use two M3 x 10 screws to fasten the mount in place.
    </td>
    <td align="center">
      <img width="450" alt="Secure the Mount" src="https://github.com/user-attachments/assets/062b63a8-7cc4-48de-85b3-37ae3f0264a0" />
    </td>
  </tr>
  <tr>
    <td>
      3. <b>Connect the Cable:</b> Plug the data cable connector into the back of the mount, paying attention to the orientation of the anti-fooling slot to ensure it connects correctly.
    </td>
    <td align="center">
      <img width="450" alt="Connect the Cable" src="https://github.com/user-attachments/assets/cee6f5b1-b98f-40af-892a-15e9c1a18dd7" />
    </td>
  </tr>
  <tr>
    <td>
      4. <b>Connect to Computer:</b> Plug the other end of the data cable (USB Type A) into a USB port on your computer. You can also use a USB Hub if necessary.
    </td>
    <td align="center">
      <img width="450" alt="Connect to Computer" src="https://github.com/user-attachments/assets/5ccb213b-9550-4a4e-9381-cd74405f6ecf" />
    </td>
  </tr>
  <tr>
</table>


#### Fixed Environment Camera

<table>
  <tr>
    <td>
      1. <b>Unscrew the Nut:</b> Remove the nut from the back of the clamp.
    </td>
    <td align="center">
      <img width="300" alt="Unscrew the Nut" src="https://github.com/user-attachments/assets/ab2a3806-7811-43c7-bfe9-4f21a365492c" />
    </td>
  </tr>
  <tr>
    <td>
      2. <b>Slide the Nut:</b> First, slide the nut over the universal ball and into the support column at the end of the bracket.
    </td>
    <td align="center">
      <img width="300" alt="Slide the Nut" src="https://github.com/user-attachments/assets/219f91a5-8d85-49a0-9e38-68a95415d712" />
    </td>
  </tr>
  <tr>
    <td>
      3. <b>Attach the Clamp:</b> Place the tail of the clamp over the universal ball.
    </td>
    <td align="center">
      <img width="300" alt="Attach the Clamp" src="https://github.com/user-attachments/assets/0a14bcfd-18bc-47be-947d-33e7b798e0ea" />
    </td>
  </tr>
  <tr>
    <td>
      4. <b>Tighten:</b> Thread the nut back onto the universal ball and tighten it from the back to secure the clamp.
    </td>
    <td align="center">
      <img width="300" alt="Tighten" src="https://github.com/user-attachments/assets/4ca206eb-0ba2-4015-a5e0-2eed4509dd77" />
    </td>
  </tr>
  <tr>
    <td>
      5. <b>Attach the Camera Stand:</b> Clamp the camera tablet stand onto the clamp.
    </td>
    <td align="center">
      <img width="300" alt="Attach the Camera Stand" src="https://github.com/user-attachments/assets/d663a4fd-1db5-4024-83f2-b9a0f24efa73" />
    </td>
  </tr>
</table>

<p>
  <b>Camera Stand Installation</b>
</p>
<table>
  <tr>
    <td>
      1. <b>Cable Management:</b> Use zip ties to secure the camera's USB cable to the vertical stand post.
    </td>
    <td align="center">
      <img width="300" alt="Cable Management" src="https://github.com/user-attachments/assets/855177db-2c7b-4776-8d92-fcb7062c352b" />
    </td>
  </tr>
  <tr>
    <td>
      2. <b>Final Installation:</b> Insert the stand into the base.
    </td>
    <td align="center">
      <img width="300" alt="Final Installation" src="https://github.com/user-attachments/assets/0b3715e9-dd99-4d1e-87ec-f60dc2061ab6" />
    </td>
  </tr>
</table>

-----

### **2. Software**

### **2.1 Camera Configuration and Data Recording**

#### Identifying Camera IDs

Before you start recording data, you need to confirm the serial numbers of your connected cameras. You can use the `benchmarks/videoio/capture_camera_feed.py` script and modify the `VideoCapture()` function's index to confirm the correspondence between the camera and its serial number.

Alternatively, you can directly run `lerobot/common/robot_devices/cameras/opencv.py`. This script will list all detectable cameras, capture some images, and save them to the `outputs/images_from_opencv_cameras` folder. You can use these images to determine which physical camera corresponds to which device ID.

**File Naming and Camera ID Correspondence**

| Filename | Corresponding Camera ID |
| :--- | :--- |
| `camera_00_frame_000000.png` | 0 |
| `camera_01_frame_000001.png` | 1 |
| `camera_02_frame_000002.png` | 2 |
| ... | ... |
| `camera_04_frame_000002.png` | 4 |

Record the correspondence between your cameras and their serial numbers. For example (this is just an example, your actual setup may vary):

  * `1` -- Hand-eye Camera (`handeye`)
  * `2` -- Fixed Environment Camera (`fixed`)

**Note:** The serial number correspondence may change after unplugging the cameras or restarting the computer.

Next, you need to modify the configuration in `lerobot/common/robot_devices/robots/configs.py`. Be sure to only edit the `class So101RobotConfig` and not any other similar classes. 

<table>
  <tr>
    <td>
      Be sure to only edit the <code>class So101RobotConfig</code> and not any other similar classes.
    </td>
    <td align="center">
      <img width="450" alt="Configuration file" src="https://github.com/user-attachments/assets/be505b5a-b286-4a3c-a402-5c582ed3c17e" />
    </td>
  </tr>
  <tr>
    <td>
      If you have a third camera, you can add another camera entry here.
    </td>
    <td align="center">
      <img width="450" alt="Adding a third camera" src="https://github.com/user-attachments/assets/194cc41c-3da7-4457-9062-394fa3d4a630" />
    </td>
  </tr>
</table>

#### Camera Encoding Stream Settings

To support a higher frame rate for cameras connected to the same hub, you need to modify `lerobot\common\robot_devices\cameras\opencv.py`. After setting the resolution width and height, add the following line to set the MJPG stream.

```python
self.camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
```

<img width="1185" height="579" alt="image" src="https://github.com/user-attachments/assets/fecc7bb0-effc-4280-b221-c2bd2acfd6f4" />

#### Local Recording

Local recording is straightforward and does not require a Hugging Face token.

First, set the `HF_USER` environment variable to your username.

  * **Linux/macOS:** `export HF_USER=your_user_name`
  * **Windows (Command Prompt):** `set HF_USER=your_user_name`

Then, use the following command to start recording:

  * **Linux/macOS:**
    ```bash
    python lerobot/scripts/control_robot.py \
      --robot.type=so101 \
      --control.type=record \
      --control.fps=30 \
      --control.single_task="Grasp a lego block and put it in the bin." \
      --control.repo_id=${HF_USER}/so101_test \
      --control.tags='["so101","tutorial"]' \
      --control.warmup_time_s=5 \
      --control.episode_time_s=30 \
      --control.reset_time_s=30 \
      --control.num_episodes=10 \
      --control.push_to_hub=false
    ```
  * **Windows (Powershell):**
    ```powershell
    python lerobot/scripts/control_robot.py `
      --robot.type=so101 `
      --control.type=record `
      --control.fps=30 `
      --control.single_task="Grasp a lego block and put it in the bin." `
      --control.repo_id=${HF_USER}/so101_test `
      --control.tags='[\"so101\",\"tutorial\"]' `
      --control.warmup_time_s=5 `
      --control.episode_time_s=30 `
      --control.reset_time_s=30 `
      --control.num_episodes=10 `
      --control.push_to_hub=false
    ```

To continue a previous recording, you can add `--control.resume=true` to the command.

#### Parameter Explanations

| Parameter | Explanation | Suggested Settings |
| :--- | :--- | :--- |
| `control.num_episodes` | The number of times to repeat the action. | |
| `control.warmup_time_s` | The time, in seconds, from when the program starts until it begins recording valid data. | Set it shorter (e.g., 2 seconds) if your preparation is quick. |
| `control.episode_time_s` | The duration of the entire task, in seconds. | |
| `control.reset_time_s` | The time, in seconds, required to reset the scene to its initial state after completing the task. | If the scene reset is fast, you can set it shorter (e.g., 5 seconds). If the scene is complex and involves resetting multiple items, a longer time is needed. |
| `control.push_to_hub=false` | Do not upload data to Hugging Face. | |

**The end of each action can be triggered in two ways:**

  * The timer reaches `episode_time_s`.
  * You press the right arrow key on the keyboard to end the current episode early if the action is completed.

#### Basic Workflow

  * Manually operate the Leader arm to complete the target action (e.g., grasp a cup).
  * The Follower arm will synchronously record the motion trajectory through the cameras.

It is recommended to first collect about 10 episodes to test the entire process. For better results, you should collect more episodes (e.g., ≥50).

### **2.2 Training Configuration**

For training your model, it is recommended for beginners to use **ACT (Action Chunking Transformers)**, which is specified by `--policy.type=act`.

Other available policies include:

  * `act`: Action Chunking Transformers
  * `diffusion`: Diffusion Policy
  * `tdmpc`: TDMPC Policy
  * `vqbet`: VQ-BeT
  * `pi0`: A Vision-Language-Action Flow Model for General Robot Control
  * `pi0fast`

For local training, add the option `--wandb.enable=false` to disable Weights & Biases logging.

To start training, run the following command:

```bash
python lerobot/scripts/train.py \
  --dataset.repo_id=${HF_USER}/so100_test \
  --policy.type=act \
  --output_dir=outputs/train/act_so100_test \
  --job_name=act_so101_test \
  --policy.device=cuda \
  --wandb.enable=false
```

When logs similar to the following appear, it indicates that training has started:

```
INFO 2025-03-01 21:03:07 ts/train.py:232 step:100 smpl:800 ep:3 epch:0.67 loss:4.547 grdn:131.117 lr:1.0e-05 updt s:0.297 data s:0.000
INFO 2025-03-01 21:03:13 ts/train.py:232 step:120 smpl:960 ep:4 epch:0.80 loss:4.117 grdn:115.125 lr:1.0e-05 updt s:0.296 data s:0.000
INFO 2025-03-01 21:03:18 ts/train.py:232 step:140 smpl:1K ep:5 epch:0.93 1oss:3.772 grdn:106.575 lr:1.0e-05 updt s:0.296 data s:0.000
```

**Note:** For 10 sets of data, training with an RTX 3090 graphics card takes approximately 2 hours.

### **2.3 Real-Time Inference Test**

#### Running the Inference Test

To test the trained model in real-time, run one of the following commands. This will use the trained policy to control the robotic arm.

  * **Ubuntu/MacOS Command:**
    ```bash
    python lerobot/scripts/control_robot.py \
      --robot.type=so101 \
      --control.type=record \
      --control.fps=30 \
      --control.single_task="Grasp a lego block and put it in the bin." \
      --control.repo_id=${HF_USER}/eval_act_so101_test \
      --control.tags='["tutorial"]' \
      --control.warmup_time_s=5 \
      --control.episode_time_s=30 \
      --control.reset_time_s=30 \
      --control.num_episodes=10 \
      --control.push_to_hub=false \
      --control.policy.path=outputs/train/act_so101_test/checkpoints/last/pretrained_model
    ```
  * **Windows Powershell Command:**
    ```powershell
    python lerobot/scripts/control_robot.py `
      --robot.type=so101 `
      --control.type=record `
      --control.fps=30 `
      --control.single_task="Grasp a lego block and put it in the bin." `
      --control.repo_id=${HF_USER}/eval_act_so101_test `
      --control.tags='[\"tutorial\"]' `
      --control.warmup_time_s=5 `
      --control.episode_time_s=30 `
      --control.reset_time_s=30 `
      --control.num_episodes=10 `
      --control.push_to_hub=false `
      --control.policy.path=outputs/train/act_so101_test/checkpoints/last/pretrained_model
    ```

#### Parameter Explanations

| Parameter | Explanation | Suggested Settings |
| :--- | :--- | :--- |
| `warmup_time_s` | The time, in seconds, from when the program starts until it begins recording valid data. | If your preparation is quick, you can set it shorter (e.g., 2 seconds). |
| `episode_time_s` | The duration of the entire task, in seconds. | |
| `reset_time_s` | The time, in seconds, required to reset the scene to its initial state after completing the task. | If the scene reset is fast, you can set it shorter (e.g., 5 seconds). If the scene is complex and involves resetting multiple items, a longer time is needed. |
| `push_to_hub=false` | Do not upload data to Hugging Face. | |
| `control.policy.path` | The path to the trained policy model. | |

#### Common Issues During Inference

  * **Robotic Arm Shaking:**
      * Adjust the `D_Coefficient` parameter in the `set_so100_robot_preset()` function within `lerobot/common/robot_devices/robots/manipulator.py`. Try reducing its value (e.g., to 0).
      * Check the servo power supply (7.4V or 12V for the Follower arm should be at least 2A).
  * **Motion Offset:**
      * Recalibrate the joint zero points.
  * **Training Failure:**
      * Reduce the `batch_size` or increase the diversity of your dataset.

---

Congratulations! You've taken the first major step into the world of embodied AI by creating your very own robot arm. This isn't just a collection of parts—it's the foundation for a future filled with possibility. The journey is just beginning, and I'll be here to guide you as we add the power of language to your robot. For now, take a moment to admire what you've built. Say hi to your new robotic partner! 🤖🚀


## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).


