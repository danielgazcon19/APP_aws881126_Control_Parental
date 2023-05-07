import requests
from bs4 import BeautifulSoup

# Leer las URLs que se deben bloquear desde un archivo de texto
with open("urls_bloqueadas.txt", "r") as f:
    urls_bloqueadas = f.readlines()
# Eliminar los saltos de línea y los espacios en blanco al final de cada línea
urls_bloqueadas = [url.strip() for url in urls_bloqueadas]

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Verificar si la URL a la que se está accediendo está en la lista de URLs bloqueadas
if url in urls_bloqueadas:
    print("No se puede acceder a esta página.")
else:
    print("La página es segura.")

# leer archivo de palabras clave
with open("palabras_clave.txt", "r") as f:
    palabras_clave = f.read().splitlines()

# solicitar url al usuario
url = input("Ingrese la URL a revisar: ")

# obtener contenido de la página
response = requests.get(url)
contenido = response.content.decode("utf-8")

# verificar si contiene palabras clave
for palabra in palabras_clave:
    if palabra.lower() in contenido.lower():
        print(f"La palabra clave '{palabra}' está en el contenido. Acceso denegado.")
        break
else:
    print("El contenido es seguro. Acceso permitido.")