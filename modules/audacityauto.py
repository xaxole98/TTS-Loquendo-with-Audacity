import os
import time
import pyautogui

def audacityauto():
    # Definir ruta de la carpeta con los archivos de audio
    audio_folder = r'C:\Users\xaxo55le\Downloads\Audios Terminados'

    # Obtener lista de archivos de audio en la carpeta
    audio_files = os.listdir(audio_folder)

    # Filtrar solo los archivos de audio con extensión .wav
    audio_files = [file for file in audio_files if file.endswith('.wav')]

    # Importar y exportar cada archivo de audio
    for audio_file in audio_files:
        # Abrir Audacity
        pyautogui.hotkey('win', 's')
        pyautogui.write('Audacity')
        pyautogui.press('enter')
        time.sleep(7)
        pyautogui.press('enter')

        # Importar archivo de audio
        pyautogui.hotkey('ctrl', 'shift', 'i')
        time.sleep(5)
        pyautogui.typewrite(os.path.join(audio_folder, audio_file))
        pyautogui.hotkey('enter')  # Seleccionar todo en la pista de audio
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'a')  # Seleccionar todo en la pista de audio
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'j')  # Ejecutar Control + | después de importar el audio
        time.sleep(40)


        # Exportar archivo como WAV con nombre basado en el archivo original
        output_folder = r'C:\Users\xaxo55le\Downloads\Audios Terminados\Audios Transiccionados'
        output_file = os.path.join(output_folder, audio_file[:-4] + '_f.wav')
        pyautogui.hotkey('ctrl', 'shift','1')
        time.sleep(5)
        pyautogui.typewrite(output_file)
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.press('enter')

        # Cerrar Audacity
        pyautogui.hotkey('alt', 'f4')
        pyautogui.press('tab')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(5)


audacityauto()