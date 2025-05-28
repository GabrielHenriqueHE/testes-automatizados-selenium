from selenium.webdriver.common.by import By
from base import BasePage


class InventoryPage(BasePage):
    def add_to_cart(self, product_name):
        self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']")

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
