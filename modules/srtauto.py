import os


def srtauto():
    ruta_script = r"C:\Users\xaxo55le\Downloads\Audios Terminados\Audios Autotune Podcast\autosrt.py"

    # Guardar el directorio actual
    directorio_original = os.getcwd()

    # Cambiar el directorio actual a la ubicación del script
    os.chdir(os.path.dirname(ruta_script))

    # Ejecutar el script
    os.system("py autosrt.py")

    # Cambiar el directorio actual de vuelta a la ubicación original
    os.chdir(directorio_original)
    
srtauto()    
