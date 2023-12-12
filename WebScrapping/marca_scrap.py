from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv


# Configurar el driver de Selenium
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Cargar la página web
driver.get("https://www.marca.com/futbol/primera-division/clasificacion.html?intcmp=MENUMIGA&s_kw=clasificacion")

# Esperar a que se cargue la tabla de clasificación
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ue-c-table-ranking")))

# Parsear el contenido HTML de la página
soup = BeautifulSoup(driver.page_source, "html.parser")

# Obtener la tabla de clasificación
table = soup.find("table", class_='ue-c-table-ranking')

# Obtener las filas de la tabla de clasificación
rows = table.find_all('tr', class_='ue-c-table-ranking__tr')

# Crear una lista para almacenar los datos de clasificación
clasificacion = []

# Recorrer las filas y obtener los datos de equipo y puntos
for row in rows:
    equipo = row.find('span', class_='ue-c-table-ranking__team-name').text.strip()
    puntos = row.find('td', class_='ue-c-table-ranking__td').text.strip()
    clasificacion.append((equipo, puntos))

# Imprimir los datos de clasificación
for equipo, puntos in clasificacion:
    print(f"Equipo: {equipo}, Puntos: {puntos}")
    
# Convertir los datos a un .csv
with open('clasificacion.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Equipo', 'Puntos'])  # Escribir encabezados
    writer.writerows(clasificacion)  # Escribir datos de clasificación

# Cerrar el driver
driver.quit()

