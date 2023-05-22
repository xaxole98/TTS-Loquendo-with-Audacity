import os
import pyttsx3

def generar_voz(ruta_texto, ruta_audio):
    # Crear objeto de la biblioteca pyttsx3
    engine = pyttsx3.init()

    # Obtener la lista de voces disponibles
    voces = engine.getProperty("voices")

    # Imprimir la lista de voces
    for idx, voz in enumerate(voces):
        print(f"Voz {idx}: {voz.name}")

    # Seleccionar la voz deseada
    voz_seleccionada = int(input("Seleccione el número de la voz deseada:\n"))
    engine.setProperty("voice", voces[voz_seleccionada].id)

    # Cambiar el tono de voz
    engine.setProperty("rate", -4000)  # valor más bajo de tasa para una voz más lenta

    # Cambiar el tempo
    engine.setProperty("rate", -300)  # valor más alto de tasa para un tempo más rápido

    # Leer el archivo de texto y generar la voz sintética
    with open(ruta_texto, "r") as archivo:
        contenido = archivo.read()
        engine.save_to_file(contenido, ruta_audio)
        engine.runAndWait()

# Definir la ruta del archivo de texto
ruta_texto = os.path.join("..", "settings", "text", "archivo.txt")

# Definir la ruta del archivo de audio a generar
ruta_audio = os.path.join("..", "loquendo", "audio.mp3")

# Llamar a la función para generar la voz
generar_voz(ruta_texto, ruta_audio)
