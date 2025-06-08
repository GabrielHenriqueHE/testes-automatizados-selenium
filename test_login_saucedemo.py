from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
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
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )

    def teardown_method(self, method):
        self.driver.quit()

    def realizar_login(self, username, password):
        sleep(1)
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        sleep(1)
        self.driver.find_element(By.ID, "password").send_keys(password)
        sleep(1)
        self.driver.find_element(By.ID, "login-button").click()
        sleep(2)

    def test_login_com_credenciais_validas(self):
        self.realizar_login("standard_user", "secret_sauce")
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("inventory")
        )
        assert "inventory" in self.driver.current_url

    def test_login_com_usuario_incorreto(self):
        self.realizar_login("usuario_errado", "secret_sauce")
        mensagem_erro = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        ).text
        assert "Username and password do not match" in mensagem_erro or "do not match" in mensagem_erro

    def test_login_com_senha_incorreta(self):
        self.realizar_login("standard_user", "senha_errada")
        mensagem_erro = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        ).text
        assert "Username and password do not match" in mensagem_erro or "do not match" in mensagem_erro

    def test_login_com_usuario_e_senha_incorretos(self):
        self.realizar_login("usuario_errado", "senha_errada")
        mensagem_erro = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        ).text
        assert "Username and password do not match" in mensagem_erro or "do not match" in mensagem_erro
