# robot-arm-guide

-----

## Welcome to the Robot Arm Guide\!

This repository serves as a comprehensive, step-by-step guide to building, configuring, and operating your **LeRobot SO-ARM101 Robotic Arm**. Our mission is to demystify robotics and AI by providing a hands-on learning experience, culminating in the implementation of advanced control techniques like **Diffusion Policy**.

Whether you're a beginner curious about robotics or an enthusiast eager to dive into imitation learning, this guide is designed to help you bring your SO-ARM101 to life and equip it with intelligent control.

-----

## Getting Started: Acquiring Your SO-ARM101

If you don't yet have a LeRobot SO-ARM101, you have a few options to get started:

  * **Build Your Own:** Explore the official GitHub repository for the SO-ARM100 (the core design for the 101) to find detailed build instructions and component lists:
    [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100)
  * **Purchase a Kit:** You can often find ready-to-assemble kits or pre-built arms on platforms like Amazon or Taobao for less than £200.

-----

## Setting Up Your Robotic Arm

Once you have your SO-ARM101 kit and components ready, let's dive into the exciting world of robotic arm control\!

### 1\. Pre-configuring Servo IDs and Parameters

Properly setting up your servo motors is a crucial first step for stable and reliable arm operation.

  * **Download the Servo Configuration Tool:**
    You'll need the `FD1.9.8.5` servo debugging tool to configure your servo IDs and parameters.
    [Download FD1.9.8.5 (250425).zip](https://gitee.com/ftservo/fddebug/blob/master/FD1.9.8.5\(250425\).zip)

  * **Follow the Configuration Tutorial:**
    ***Please Note:*** The provided link for the tutorial (`https://www.youtube.com/watch?v=70GuJf2jbYk`) appears to be incomplete or incorrect. While this guide aims to be comprehensive, specific servo configuration steps can vary slightly. We recommend looking for official documentation or video tutorials related to `FD1.9.8.5` or `FeiTeng (FTServo)` servos on YouTube or within the `TheRobotStudio` community. We will update this section with a verified tutorial as soon as possible.

    *Typical configuration involves connecting each servo to the tool, assigning a unique ID (e.g., 1 through 6 for a 6-DOF arm), and setting parameters like the rotation limits or initial position.*

-----

## What's Next in this Guide?

This guide will progressively lead you through:

  * **Hardware Assembly & Wiring:** Detailed instructions for putting your SO-ARM101 together.
  * **Basic Control & Calibration:** Getting your arm to move with simple commands.
  * **Software Environment Setup:** Preparing your computer for advanced robotics development (Python, relevant libraries).
  * **Introduction to Diffusion Policy:** Understanding the theory behind this powerful imitation learning technique.
  * **Implementing Diffusion Policy:** Practical steps to collect data, train models, and deploy Diffusion Policy on your SO-ARM101 for various tasks.
  * **Troubleshooting & Advanced Tips:** Common issues and how to resolve them.

-----

## Contributing

We welcome contributions to make this guide even better\! If you have suggestions, corrections, or want to add a new section (e.g., a verified servo configuration tutorial\!), please feel free to open an issue or submit a pull request.

-----

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
