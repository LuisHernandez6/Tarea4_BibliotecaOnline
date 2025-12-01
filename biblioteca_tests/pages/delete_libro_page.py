from selenium.webdriver.common.by import By

class DeleteLibroPage:
    def __init__(self, driver):
        self.driver = driver

    def confirmar(self):
        self.driver.find_element(By.ID, "btnConfirmar").click()

    def cancelar(self):
        self.driver.find_element(By.LINK_TEXT, "Cancelar").click()
