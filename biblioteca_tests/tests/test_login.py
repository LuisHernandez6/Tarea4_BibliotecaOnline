import pytest
from utils.base_test import BaseTest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestLogin(BaseTest):

    def test_login_correcto(self):
        login = LoginPage(self.driver)
        login.go_to(self.base_url)
        login.login("admin", "admin@mail.com", "1234")

        WebDriverWait(self.driver, 10).until(
            lambda d: "/Libros" in d.current_url
        )
        assert "/Libros" in self.driver.current_url

    def test_login_incorrecto(self):
        login = LoginPage(self.driver)
        login.go_to(self.base_url)
        login.login("admin", "admin@mail.com", "wrongpassword")
    
        mensaje = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mensaje"))
        )
        assert "Credenciales incorrectas" in self.driver.page_source

    def test_login_campos_vacios(self):
        login = LoginPage(self.driver)
        login.go_to(self.base_url)
        login.login("", "", "")
        time.sleep(0.1)
        assert "required" in self.driver.page_source
