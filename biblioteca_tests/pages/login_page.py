from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, base_url):
        self.driver.get(base_url + "/Account/Login")

    def login(self, nombreUsuario, email, password):
        self.driver.find_element(By.NAME, "nombreUsuario").clear()
        self.driver.find_element(By.NAME, "nombreUsuario").send_keys(nombreUsuario)

        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(email)

        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys(password)

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
