import pytest
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from pages.libros_page import LibrosPage
from pages.delete_libro_page import DeleteLibroPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestEliminarLibro(BaseTest):

    def login_admin(self):
        login = LoginPage(self.driver)
        login.go_to(self.base_url)
        login.login("admin", "admin@mail.com", "1234")

    def test_eliminar_libro_correcto(self):
        self.login_admin()
        libros = LibrosPage(self.driver)
        libros.delete_first()

        delete = DeleteLibroPage(self.driver)
        delete.confirmar()

        mensaje = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mensaje"))
        )

        assert "eliminado" in self.driver.page_source.lower()

    def test_cancelar_eliminacion(self):
        self.login_admin()
        libros = LibrosPage(self.driver)
        libros.delete_first()

        delete = DeleteLibroPage(self.driver)
        delete.cancelar()

        # Regresa a Index
        assert "/Libros/Index" in self.driver.current_url
