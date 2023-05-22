import os
from pydub import AudioSegment
from pydub.playback import play
import simpleaudio

def changeloquendo():
    # Definir la ruta del archivo de audio generado por pyttsx3
    ruta_audio = os.path.join("..", "loquendo", "audio.mp3")

    # Cargar el archivo de audio utilizando pydub
    audio = AudioSegment.from_file(ruta_audio)

    # Cambiar el tono de voz
    new_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate * 0.9543126816935)}) # Bajar la frecuencia en un semitono

    # Realce de graves a nivel de -3dB
    new_audio = new_audio.low_pass_filter(8000)

    # Normalizar el audio
    new_audio = new_audio.normalize()

    # Convertir el sample rate del audio a un valor soportado
    new_audio = new_audio.set_frame_rate(44100)

    # Reproducir el audio resultante

    # Exportar el audio resultante a un archivo WAV
    new_audio.export(os.path.join("..", "loquendo", "audio_procesado.wav"), format="wav")
    
changeloquendo()