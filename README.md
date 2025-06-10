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

### SO-100 Follower Arm Kit

If you already own a VR headset, you might find the SO-100 follower arm kit particularly useful. This kit, which does not include the leader arm, is available from:

* **Phospho:** [robots.phospho.ai](https://robots.phospho.ai)

### 1.2 Setting Up Your Robotic Arm

Once you have your SO-ARM101 kit and components ready, let's dive into the exciting world of robotic arm control!

1. Pre-configuring Servo IDs and Parameters

Properly setting up your servo motors is a crucial first step for stable and reliable arm operation.

* **Download the Servo Configuration Tool:**
    You'll need the `FD1.9.8.5` servo debugging tool to configure your servo IDs and parameters.
    [Download FD1.9.8.5 (250425).zip](https://gitee.com/ftservo/fddebug/blob/master/FD1.9.8.5\(250425\).zip)
    You should be able to see a page like below:
    ![image](https://github.com/user-attachments/assets/c2102d50-6846-43e8-a11e-6e051fc7278d)

* **Follow the Configuration Tutorial:**
    [LeRobot SO-ARM101 Robotic Arm - Assembly and Setup Guide](https://www.youtube.com/watch?v=70GuJf2jbYk)

---

## Contributing

We welcome contributions to make this guide even better! If you have suggestions, corrections, or want to add a new section (e.g., a verified servo configuration tutorial!), please feel free to open an issue or submit a pull request.

---

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
