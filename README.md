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

If you don't yet have a LeRobot SO-ARM101, you have a few options to get started:

- **Build it Yourself**
   - Source the components from the [Bill of Materials](#sourcing-parts).
   - 3D print the parts (or order the 3D printed parts), explained in [Printing the Parts](#printing-the-parts).
   - Follow our [Assembly Guide](https://huggingface.co/docs/lerobot/so101).
- **Buy a Kit**
   - Buy assembled arms or a parts kit from one of the vendors [here](#kits).
   - Optionally follow our [Assembly Guide](https://huggingface.co/docs/lerobot/so101).

---

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
