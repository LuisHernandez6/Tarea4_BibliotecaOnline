import pytest
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.libros_page import LibrosPage
from pages.create_libro_page import CreateLibroPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestCrearLibro(BaseTest):

    def login_admin(self):
        login = LoginPage(self.driver)
        login.go_to(self.base_url)
        login.login("admin", "admin@mail.com", "1234")

    def test_crear_libro_correcto(self):
        self.login_admin()
        libros = LibrosPage(self.driver)
        libros.go_to_create()
        create = CreateLibroPage(self.driver)
        create.crear_libro("Nuevo Libro Selenium", "Luis Hernandez", "29.99", "10")

        mensaje = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mensaje"))
        )
        assert "Libro creado correctamente." in self.driver.page_source

    def test_crear_libro_campos_vacios(self):
        self.login_admin()
        libros = LibrosPage(self.driver)
        libros.go_to_create()
        create = CreateLibroPage(self.driver)
        create.crear_libro("", "", "", "")
        time.sleep(0.1)
        assert "The Titulo field is required" in self.driver.page_source
