# Model-Based Embedded Fault Detection System

## Demo Videos

- Arduino IDE demo: https://youtube.com/shorts/Jpcqe5twYGc?feature=share
- Python code demo: https://youtube.com/shorts/VAUeTeP_f00?feature=share

## Prototype Note

The initial live prototype demo used direct jumper-wire connections from the analog joystick module to the Arduino Uno rather than a breadboard. The joystick provided a real analog input, and the Arduino sampled the signal on A0 in real time.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge" alt="Python 3.x">
  <img src="https://img.shields.io/badge/MATLAB-R2024b-orange?style=for-the-badge" alt="MATLAB R2024b">
  <img src="https://img.shields.io/badge/KiCad-8-3d7fff?style=for-the-badge" alt="KiCad 8">
  <img src="https://img.shields.io/badge/MathWorks-Certified-0053a0?style=for-the-badge" alt="MathWorks Certified">
</p>

A real-hardware fault detection system: the current live prototype uses a direct-wired analog joystick module feeding an Arduino Uno on A0, with Python handling the downstream processing and classification pipeline. The repo also documents the Simscape digital twin, Stateflow fault logic, and the planned KiCad sensor front-end.

## Current Prototype

The recorded demo shows a real analog signal path from the joystick module into the Arduino Uno, sampled live on A0 and streamed into the Python workflow for analysis.

## Technical Glossary

This project uses terms from HIL testing, edge computing, DSP, power integrity, and PCB design.  
See the Jargon to English glossary here:
<p align="center">
  <a href="docs/glossary.md">
    <img src="https://img.shields.io/badge/START_HERE-Technical_Glossary-ff6b00?style=for-the-badge&logo=github&logoColor=white" alt="Start Here - Technical Glossary">
  </a>
</p>
