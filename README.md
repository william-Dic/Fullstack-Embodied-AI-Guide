<h1 align="center">Fullstack Embodied AI Guide</h1>

<p align="center">
  <img width="300" alt="f939a2605d4f7fcccc692090e379753" src="https://github.com/user-attachments/assets/6145c4a7-bf46-4650-b57c-e90c18fe220e" />
</p>

## **Ready to launch into robotics?** 🤖🚀
This guide is your **ultimate starting point** for bringing **embodied AI** to **life/Your Home**🏠! We'll walk you through everything: from **building your robot** from scratch to equipping it with **cutting-edge AI control techniques** like **Diffusion Policy** and **ACT**. 🧠✨

Whether you're a beginner curious about robots or eager to explore advanced AI, get ready for a **hands-on learning adventure** that makes complex concepts **simple and fun!** 🌟🛠️

---

## Table of Contents

### 1. Hardware

* 1.1 [Getting Started: Acquiring Your SO-ARM101](#getting-started-acquiring-your-so-arm101)
* 1.2 [Setting Up Your Robotic Arm](#setting-up-your-robotic-arm)
    * [Pre-configuring Servo IDs and Parameters](#pre-configuring-servo-ids-and-parameters)
    * [Download the Servo Configuration Tool](https://gitee.com/ftservo/fddebug/blob/master/FD1.9.8.5\(250425\).zip)
    * [Follow the Configuration Tutorial](https://www.youtube.com/watch?v=70GuJf2jbYk)
* [Hardware Assembly & Wiring](#hardware-assembly--wiring)
* [Basic Control & Calibration](#basic-control--calibration)

### 2. Software

* 2.1 [Software Environment Setup](#software-environment-setup)
* [Introduction to Diffusion Policy](#introduction-to-diffusion-policy)
* [Implementing Diffusion Policy](#implementing-diffusion-policy)
* [Troubleshooting & Advanced Tips](#troubleshooting--advanced-tips)

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

### 1.5 Joint Calibration


## Contributing

We welcome contributions to make this guide even better! If you have suggestions, corrections, or want to add a new section (e.g., a verified servo configuration tutorial!), please feel free to open an issue or submit a pull request.

---

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
