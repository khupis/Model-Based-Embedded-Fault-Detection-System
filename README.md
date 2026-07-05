# Model-Based Embedded Fault Detection System

## Demo Videos

- Arduino IDE demo: https://youtube.com/shorts/Jpcqe5twYGc?feature=share
- Python code demo: https://youtube.com/shorts/VAUeTeP_f00?feature=share

## Current Hardware Prototype

The recorded prototype used direct jumper-wire connections from the analog joystick module to the Arduino Uno. The joystick module fed a real analog signal, and the Arduino sampled that signal on A0 in real time.

<p align="center">
  <img src="images/Arduino1.jpg" alt="Analog joystick module connected to the Arduino Uno prototype" width="250">
  <img src="images/Arduino2.jpg" alt="Top view of the Arduino Uno with direct-wired joystick prototype" width="250">
</p>

<p align="center">
  <img src="images/Arduino3.jpg" alt="Arduino Uno power and analog input side with wiring" width="250">
  <img src="images/Arduino4.jpg" alt="Board-side wiring view of the direct-wired prototype" width="250">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge" alt="Python 3.x">
  <img src="https://img.shields.io/badge/MATLAB-R2024b-orange?style=for-the-badge" alt="MATLAB R2024b">
  <img src="https://img.shields.io/badge/KiCad-8-3d7fff?style=for-the-badge" alt="KiCad 8">
  <img src="https://img.shields.io/badge/MathWorks-Certified-0053a0?style=for-the-badge" alt="MathWorks Certified">
</p>

A real-hardware fault detection system: the current live prototype uses a direct-wired analog joystick module feeding an Arduino Uno on A0, with Python handling the downstream processing and classification pipeline. The repo also documents the Simscape digital twin, Stateflow fault logic, and the planned KiCad sensor front-end.

## Technical Glossary

This project uses terms from HIL testing, edge computing, DSP, power integrity, and PCB design.  
See the Jargon to English glossary here:
<p align="center">
  <a href="docs/glossary.md">
    <img src="https://img.shields.io/badge/START_HERE-Technical_Glossary-ff6b00?style=for-the-badge&logo=github&logoColor=white" alt="Start Here - Technical Glossary">
  </a>
</p>
