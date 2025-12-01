from selenium.webdriver.common.by import By

class CreateLibroPage:
    def __init__(self, driver):
        self.driver = driver

    def crear_libro(self, titulo, autor, precio, stock):
        self.driver.find_element(By.ID, "Titulo").clear()
        self.driver.find_element(By.ID, "Titulo").send_keys(titulo)

        self.driver.find_element(By.ID, "Autor").clear()
        self.driver.find_element(By.ID, "Autor").send_keys(autor)

        self.driver.find_element(By.ID, "Precio").clear()
        self.driver.find_element(By.ID, "Precio").send_keys(precio)

        self.driver.find_element(By.ID, "Stock").clear()
        self.driver.find_element(By.ID, "Stock").send_keys(stock)

        self.driver.find_element(By.ID, "btnCrearLibro").click()
