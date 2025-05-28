from selenium.webdriver.common.by import By
from base import BasePage


class CartPage(BasePage):
    def remove_product(self, product_name):
        self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']")

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        