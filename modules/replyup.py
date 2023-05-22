from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.firefox.service import Service
import re
import time

def eudio():
    def obtener_ultima_enumeracion(ruta_destino):
        ultimo_numero = 0
        for nombre_archivo in os.listdir(ruta_destino):
            coincidencia = re.match(r"(\d+)\.wav", nombre_archivo)
            if coincidencia:
                numero = int(coincidencia.group(1))
                if numero > ultimo_numero:
                    ultimo_numero = numero
        return ultimo_numero

    ruta_origen = 'C:\\Users\\xaxo55le\\Downloads\\Audios Terminados\\Audios Transiccionados'
    ruta_destino = 'C:\\Users\\xaxo55le\\Downloads\\Audios Terminados\\Audios Autotune Podcast'

    options = webdriver.FirefoxOptions()
    options.profile = webdriver.FirefoxProfile(profile_directory='C:\\Users\\xaxo55le\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\hjpne5ja.default-release-1675823868628')

    driver_service = Service(executable_path='./geckodriver.exe')
    driver = webdriver.Firefox(service=driver_service, options=options)


    for nombre_archivo in os.listdir(ruta_origen):
        if nombre_archivo.endswith('.wav'):
            wait = WebDriverWait(driver, 10)
            driver.get('https://podcast.adobe.com/enhance')
            ruta_audio = os.path.join(ruta_origen, nombre_archivo)
            upload_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))
            upload_button.send_keys(ruta_audio)

            wait = WebDriverWait(driver, 4000)
            download_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.sc-eSNLA-D.bvJLSQ')))

            nombre_archivo_descarga = download_link.get_attribute("download")

            download_link.click()

            time.sleep(10)

            ultima_enumeracion = obtener_ultima_enumeracion(ruta_destino)

            nueva_enumeracion = ultima_enumeracion + 1
            extension = os.path.splitext(nombre_archivo_descarga)[1]
            nombre_nuevo_archivo = f"{nueva_enumeracion}{extension}"

            ruta_descarga = os.path.join(os.path.expanduser('~'), 'Downloads', nombre_archivo_descarga)
            ruta_destino_nuevo = os.path.join(ruta_destino, nombre_nuevo_archivo)
            os.replace(ruta_descarga, ruta_destino_nuevo)
            driver.quit()
eudio()