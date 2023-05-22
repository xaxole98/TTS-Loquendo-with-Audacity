import os
import shutil
import send2trash

def movetrash():
    # Rutas de los archivos
    ruta_1 = r"C:\Users\xaxo55le\Downloads\Audios Terminados\1.wav"
    ruta_1_f = r"C:\Users\xaxo55le\Downloads\Audios Terminados\Audios Transiccionados\1_f.wav"
    ruta_basura = r"C:\Users\xaxo55le\Downloads\Audios Terminados\Basura"

    # Movemos los archivos a la carpeta basura
    shutil.move(ruta_1, ruta_basura)
    shutil.move(ruta_1_f, ruta_basura)

    # Enviamos los archivos a la papelera de reciclaje
    for archivo in os.listdir(ruta_basura):
        archivo_path = os.path.join(ruta_basura, archivo)
        send2trash.send2trash(archivo_path)

movetrash()