from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPageCheckout:

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

        # LOGIN uma única vez
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

    def test_checkout_correto(self):

        # Selecionar produto e adicionar ao carrinho
        sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Acessar carrinho
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Iniciar checkout
        sleep(1)
        self.driver.find_element(By.ID, "checkout").click()

        # Preencher informações obrigatórias
        sleep(1)
        self.driver.find_element(By.ID, "first-name").send_keys("Gabriel")
        sleep(1)
        self.driver.find_element(By.ID, "last-name").send_keys("Evaristo")
        sleep(1)
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")

        sleep(1)
        self.driver.find_element(By.ID, "continue").click()

        # Finalizar compra
        sleep(1)
        self.driver.find_element(By.ID, "finish").click()

        # Verificar mensagem de sucesso
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        ).text

        assert "THANK YOU FOR YOUR ORDER" in str(success_message).upper()

    def test_checkout_sem_produto(self):
        # Acessar carrinho sem adicionar produto
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verifica se carrinho está vazio
        sleep(1)
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 0, "Carrinho deveria estar vazio"

    def test_checkout_sem_dados(self):
        # Selecionar produto
        sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Acessar carrinho
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Iniciar checkout
        sleep(1)
        self.driver.find_element(By.ID, "checkout").click()

        # Deixar dados faltando e tentar prosseguir
        sleep(1)
        self.driver.find_element(By.ID, "first-name").send_keys("Gabriel")
        # last-name e postal-code faltando

        sleep(1)
        self.driver.find_element(By.ID, "continue").click()

        # Verificar mensagem de erro
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
        ).text

        assert "Error" in error_message

    def test_checkout_sem_produtos_sem_dados(self):

        # Acessar carrinho sem adicionar produto
        sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verifica se carrinho está vazio
        sleep(1)
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 0, "Carrinho deveria estar vazio"

        sleep(1)
        self.driver.find_element(By.ID, "checkout").click()

        # Deixar dados faltando e tentar prosseguir
        sleep(1)
        self.driver.find_element(By.ID, "continue").click()

        # Verificar mensagem de erro
        error_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
        ).text

        sleep(1)

        assert "Error" in error_message