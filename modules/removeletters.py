import os
import re

# Definir la ruta del archivo de texto
ruta_texto = os.path.join("..","settings", "text", "archivo.txt")

# Leer el contenido del archivo
with open(ruta_texto, "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Reemplazar "ción" por "sion"
texto_modificado1 = re.sub("í", "i", texto)
texto_modificado2= re.sub("é", "e", texto_modificado1)
texto_modificado3= re.sub("á", "a", texto_modificado2)
texto_modificado4= re.sub("ñ", "ny", texto_modificado3)
texto_modificado5= re.sub("ó", "o", texto_modificado4)
texto_modificado6= re.sub("ú", "u", texto_modificado5)
texto_modificado7= re.sub(r"\!", "", texto_modificado6)
texto_modificado8= re.sub(r"\¡", "", texto_modificado7)
texto_modificado9= re.sub("z", "s", texto_modificado8)


# Escribir el contenido modificado en el mismo archivo
with open(ruta_texto, "w", encoding="utf-8") as archivo:
    archivo.write(texto_modificado9)

print("El archivo se ha modificado con éxito.")
