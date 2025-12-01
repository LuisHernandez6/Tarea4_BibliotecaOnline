import pytest
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.libros_page import LibrosPage
from selenium.webdriver.common.by import By
import time

class TestListarLibros(BaseTest):

    def login_admin(self):
        login = LoginPage(self.driver)
        login.go_to(self.base_url)
        login.login("admin", "admin@mail.com", "1234")

    def test_ver_lista_libros(self):
        self.login_admin()
        page = LibrosPage(self.driver)

        time.sleep(0.3)

        tabla = self.driver.find_element(By.ID, "tablaLibros")
        filas = tabla.find_elements(By.TAG_NAME, "tr")

        # Debe existir mínimo el header
        assert len(filas) >= 1

    #def test_tabla_vacia(self):
        #self.login_admin()

        # Simulación: borrar datos manualmente antes del test
        # O validar comportamiento cuando no hay filas en <tbody>

        #time.sleep(0.3)

        #cuerpo = self.driver.find_element(By.CSS_SELECTOR, "table tbody")
        #filas = cuerpo.find_elements(By.TAG_NAME, "tr")

        # La tabla puede estar vacía si no hay libros
        #assert isinstance(filas, list)
