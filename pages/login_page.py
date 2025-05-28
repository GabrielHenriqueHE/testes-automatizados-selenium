from selenium.webdriver.common.by import By
from base import BasePage

class LoginPage(BasePage):
    BASE_URL = "https://www.saucedemo.com"

    def open(self):
        self.driver.get(self.BASE_URL)

    def login(self, username: str, password: str):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
