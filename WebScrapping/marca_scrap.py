from bs4 import BeautifulSoup
import pandas as pd
import requests


url = "https://www.marca.com/futbol/primera-division/clasificacion.html?intcmp=MENUMIGA&s_kw=clasificacion"

# Realizar la solicitud GET al sitio web
response = requests.get(url)


# Parsear el contenido HTML de la respuesta
soup = BeautifulSoup(response.text, "html.parser")

# Obtener la tabla de clasificación
table = soup.find('table', id='ueTableRanking')

print(table)

