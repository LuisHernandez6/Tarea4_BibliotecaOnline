from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LibrosPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_create(self):
        # Esperar hasta que el enlace sea clickable
        wait = WebDriverWait(self.driver, 10)  # espera hasta 10 segundos
        crear_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Crear Nuevo Libro"))
        )
        crear_link.click()

    def edit_first(self):
        wait = WebDriverWait(self.driver, 10)
        editar_links = wait.until(
            EC.presence_of_all_elements_located((By.LINK_TEXT, "Editar"))
        )
        editar_links[0].click()

    def delete_first(self):
        wait = WebDriverWait(self.driver, 10)
        eliminar_links = wait.until(
            EC.presence_of_all_elements_located((By.LINK_TEXT, "Eliminar"))
        )
        eliminar_links[0].click()

    def tabla_visible(self):
        return self.driver.find_element(By.TAG_NAME, "table").is_displayed()
