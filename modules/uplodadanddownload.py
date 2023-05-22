from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.firefox.service import Service
import re
import time

def enhance_audio():
    def obtener_ultima_enumeracion(ruta_destino):
        """Obtiene el último número de enumeración utilizado en los archivos de la carpeta especificada"""
        ultimo_numero = 0
        for nombre_archivo in os.listdir(ruta_destino):
            # Buscar archivos con nombres en el formato "1.wav"
            coincidencia = re.match(r"(\d+)\.wav", nombre_archivo)
            if coincidencia:
                numero = int(coincidencia.group(1))
                if numero > ultimo_numero:
                    ultimo_numero = numero
        return ultimo_numero


    # Definir la ruta del archivo de audio generado por pyttsx3
    ruta_audio = "D:\\Trabajo\\Codigos\\Videos Automaticos\\loquendo\\audio_procesado.wav"

    # Cargar el perfil de Firefox
    options = webdriver.FirefoxOptions()
    options.profile = webdriver.FirefoxProfile(profile_directory='C:\\Users\\xaxo55le\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\hjpne5ja.default-release-1675823868628')


    # Inicializar el controlador de Selenium para el navegador Firefox con el perfil cargado
    driver_service = Service(executable_path='./geckodriver.exe')
    driver = webdriver.Firefox(service=driver_service, options=options)

    # Navegar a la página web de https://podcast.adobe.com/enhance
    driver.get('https://podcast.adobe.com/enhance')

    # Esperar a que se cargue la página
    wait = WebDriverWait(driver, 6)
    upload_button = wait.until(EC.presence_of_element_located((By.ID, 'enhance-file-upload')))
    upload_button.send_keys(ruta_audio)

    # Encontrar el botón de descarga de archivo y hacer clic en él
    wait = WebDriverWait(driver, 9000)
    download_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.sc-eSNLA-D.bvJLSQ')))

    # Guardar el nombre del archivo descargado
    nombre_archivo_descarga = download_link.get_attribute("download")

    # Hacer clic en el botón de descarga
    download_link.click()

    # Esperar a que se descargue el archivo (en este caso, se espera 10 segundos)
    time.sleep(10)

    # Obtener ruta_destino

    ruta_destino = 'C:\\Users\\xaxo55le\\Downloads\\Audios Terminados'

    # Obtener la última enumeración utilizada
    ultima_enumeracion = obtener_ultima_enumeracion(ruta_destino)

    # Incrementar la enumeración y renombrar el archivo descargado
    nueva_enumeracion = ultima_enumeracion + 1
    nombre_archivo = "audio_procesado (enhanced).wav"
    extension = os.path.splitext(nombre_archivo)[1]
    nombre_nuevo_archivo = f"{nueva_enumeracion}{extension}"

    # Mover el archivo descargado a la carpeta de Audios Terminados con el nuevo nombre
    ruta_descarga = os.path.join(os.path.expanduser('~'), 'Downloads', nombre_archivo)
    ruta_destino_nuevo = os.path.join(ruta_destino, nombre_nuevo_archivo)
    os.replace(ruta_descarga, ruta_destino_nuevo)
    driver.quit()
    
enhance_audio()