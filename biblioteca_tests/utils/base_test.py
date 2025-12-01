# base_test.py
from selenium import webdriver
import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--ignore-certificate-errors")  # Ignorar errores de certificado

        self.driver = webdriver.Chrome(options=options)

        self.base_url = "https://localhost:7210"  # Cambiar segun el puerto

        yield  # pytest ejecuta la prueba

        if hasattr(self, "driver") and self.driver:
            self.driver.quit()
