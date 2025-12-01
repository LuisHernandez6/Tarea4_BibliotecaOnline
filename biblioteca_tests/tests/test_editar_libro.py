import pytest
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.libros_page import LibrosPage
from pages.edit_libro_page import EditLibroPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestEditarLibro(BaseTest):

    def login_admin(self):
        login = LoginPage(self.driver)
        login.go_to(self.base_url)
        login.login("admin", "admin@mail.com", "1234")

    def test_editar_libro_correcto(self):
        self.login_admin()
        libros = LibrosPage(self.driver)
        libros.edit_first()

        edit = EditLibroPage(self.driver)
        edit.editar_libro("Libro Editado", "Autor Editado", "15.50", "20")

        mensaje = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mensaje"))
        )

        assert "actualizado" in self.driver.page_source.lower()

    def test_editar_campos_vacios(self):
        self.login_admin()
        libros = LibrosPage(self.driver)
        libros.edit_first()

        edit = EditLibroPage(self.driver)
        edit.editar_libro("", "", "", "")
        time.sleep(0.1)
        assert "The Titulo field is required" in self.driver.page_source

    def test_editar_limites(self):
        self.login_admin()
        
        # Abrir el formulario de edición del primer libro
        libros = LibrosPage(self.driver)
        libros.edit_first()

        edit = EditLibroPage(self.driver)
        
        # Valores limite
        titulo_limite = "T" * 201
        autor_limite = "A" * 101
        precio_valido = "-1"
        stock_valido = "99999"
        
        edit.editar_libro(titulo_limite, autor_limite, precio_valido, stock_valido)
        
        # Comprobar que los valores no se realizo ningun cambio
        assert "/Libros/Edit/" in self.driver.current_url

