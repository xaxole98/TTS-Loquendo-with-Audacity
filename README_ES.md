# Generador de Texto a Voz / Text-to-Speech Generator

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)[![Telegram](https://img.shields.io/badge/Telegram-xaxole98-blue.svg)](https://t.me/xaxole98)

## Language / Idioma
- [English](README.md)
- [Español](README_ES.md)

Este proyecto tiene como objetivo proporcionar un código en Python que te permita generar voz sintética a partir de texto utilizando la biblioteca pyttsx3. Ofrece opciones de personalización para seleccionar la voz, ajustar la velocidad y generar archivos de salida.

## Características

- Selección de Voz: El código te permite elegir entre una lista de voces disponibles compatibles con la biblioteca pyttsx3. Cada voz tiene un identificador único, y puedes especificar la voz deseada seleccionando el número correspondiente.

- Ajuste de Velocidad de Voz: Puedes controlar la velocidad del habla sintética ajustando la propiedad de tasa (rate). Un valor de tasa más bajo hace que la voz sea más lenta, mientras que un valor más alto la hace más rápida.

- Conversión de Texto a Voz: El código lee el texto de un archivo especificado y genera el habla sintética correspondiente utilizando la voz y la configuración de velocidad seleccionadas. El habla de salida se guarda como un archivo de audio en la ubicación deseada.

## Requisitos previos

Antes de ejecutar este código, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- Paquetes especificados en el archivo `requirements.txt`

## Dependencias

- [pyautogui](https://pypi.org/project/PyAutoGUI/): Versión 0.9.53
- [pydub](https://pypi.org/project/pydub/): Versión 0.25.1
- [pyttsx3](https://pypi.org/project/pyttsx3/): Versión 2.90
- [selenium](https://pypi.org/project/selenium/): Versión 4.9.1
- [Send2Trash](https://pypi.org/project/Send2Trash/): Versión 1.8.0
- [simpleaudio](https://pypi.org/project/simpleaudio/): Versión 1.0.4

## Uso

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias utilizando `pip` o cualquier otro gestor de paquetes de Python. Puedes ejecutar el siguiente comando: `pip install -r requirements.txt`.
3. Modifica el código para proporcionar las rutas de archivo adecuadas para la entrada de texto y la salida de audio.
4. Ejecuta el código y sigue las instrucciones para seleccionar la voz deseada y ajustar la velocidad de la voz.
5. El código generará la voz sintética y la guardará como un archivo de audio en la ubicación especificada.

¡Disfruta generando voz sintética a partir de texto con la biblioteca pyttsx3!

Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en contactarnos.