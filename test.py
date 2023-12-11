# Prueba de automatización de tarea de descarga de archivo

import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.example.com")

    def test_download(self):
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(15)

# Siempre buscar el id del botón en el código fuente de la página. Es decir, si veos que el elementID es "login", buscar en el código fuente de la página el elemento con id="login"

        # Click en el botón Sign in
        driver.find_element_by_class_name("login").click()

        # Ingresar email y password (en caso de necesitar usuario en vez de email, usar el id "username" o el que corresponda)
        driver.find_element_by_id("email").send_keys("example@example.com")
        driver.find_element_by_id("passwd").send_keys("password")

        # Click en el botón Sign in para iniciar sesión
        driver.find_element_by_id("SubmitLogin").click()

        # Navegar a la página de descargas
        driver.find_element_by_link_text("Downloads").click()

        # Descargar el archivo
        driver.find_element_by_link_text("Download").click()
        
        # Establecer la carpeta de destino del archivo descargado
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", "/path/to/downloaded/file")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.manager.focusWhenStarting", False)
        profile.set_preference("browser.download.useDownloadDir", True)

        # Esperar 5 segundos para que se complete la descarga
        time.sleep(5)

        # Verificar que el archivo se haya descargado correctamente
        downloaded_file_path = "/path/to/downloaded/file"
        self.assertTrue(os.path.exists(downloaded_file_path))

        # Eliminar el archivo descargado
        os.remove(downloaded_file_path)
        
    # Cerrar el navegador (Opcional)
    def tearDown(self):
        self.driver.quit()