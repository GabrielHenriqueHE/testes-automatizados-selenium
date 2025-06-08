from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:

    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        sleep(1)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        sleep(1)
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        sleep(1)
        self.driver.find_element(By.ID, "login-button").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    def teardown_method(self, method):
        self.driver.quit()

    def test_logout_autenticado_com_sucesso(self):
        sleep(1)
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        sleep(1)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        assert self.driver.current_url == "https://www.saucedemo.com/"

    def test_logout_nao_realizado(self):
        sleep(2)
        assert "inventory" in self.driver.current_url
        assert self.driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()
