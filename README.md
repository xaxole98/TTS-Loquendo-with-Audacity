# Text-to-Speech Generator / Generador de Texto a Voz

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)[![Telegram](https://img.shields.io/badge/Telegram-xaxole98-blue.svg)](https://t.me/xaxole98)

## Language / Idioma
- [English](README.md)
- [Español](README_ES.md)

This project aims to provide a Python code that allows you to generate synthetic speech from text using the pyttsx3 library. It provides customization options for voice selection, voice speed, and output file generation.

## Features

- Voice Selection: The code allows you to choose from a list of available voices supported by the pyttsx3 library. Each voice has a unique identifier, and you can specify the desired voice by selecting the corresponding number.

- Voice Speed Adjustment: You can control the speed of the synthesized speech by adjusting the rate property. A lower rate value makes the voice slower, while a higher value makes it faster.

- Text-to-Speech Conversion: The code reads the text from a specified file and generates the corresponding synthetic speech using the selected voice and speed settings. The output speech is saved as an audio file in the desired location.

## Prerequisites

Before running this code, make sure you have the following dependencies installed:

- Python 3.x
- Packages specified in the `requirements.txt` file

## Dependencies

- [pyautogui](https://pypi.org/project/PyAutoGUI/): Version 0.9.53
- [pydub](https://pypi.org/project/pydub/): Version 0.25.1
- [pyttsx3](https://pypi.org/project/pyttsx3/): Version 2.90
- [selenium](https://pypi.org/project/selenium/): Version 4.9.1
- [Send2Trash](https://pypi.org/project/Send2Trash/): Version 1.8.0
- [simpleaudio](https://pypi.org/project/simpleaudio/): Version 1.0.4

## Usage

1. Clone this repository to your local machine.
2. Install the necessary dependencies using `pip` or any other Python package manager. You can run the following command: `pip install -r requirements.txt`.
3. Modify the code to provide the appropriate file paths for the text input and audio output.
4. Run the code and follow the instructions to select the desired voice and adjust the voice speed.
5. The code will generate the synthetic speech and save it as an audio file in the specified location.

Enjoy generating synthetic speech from text using the pyttsx3 library!

If you have any questions or need further assistance, feel free to contact us.