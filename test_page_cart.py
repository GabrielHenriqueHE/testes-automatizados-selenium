import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestPageCart:
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
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)  # garantir que carregou a página dos produtos

    def teardown_method(self, method):
        self.driver.quit()

    def test_pageCart(self):
        driver = self.driver

        # Já está na página de produtos por conta do login no setup

        # 3. Adicionar 3 produtos
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        time.sleep(1)

        # 4. Ir para o carrinho
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)

        # 5. Remover os produtos
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bolt-t-shirt\"]").click()
        time.sleep(1)

        # 6. Verificar se o carrinho está vazio
        items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) == 0, f"Erro: Esperado carrinho vazio, mas ainda tem {len(items)} item(ns)"
        time.sleep(2)

        # 7. Voltar para a página de produtos
        driver.find_element(By.ID, "continue-shopping").click()

        time.sleep(2)

    def test_carrinho_vazio_sem_adicionar(self):
        driver = self.driver

        # Já está na página de produtos (catálogo)

        # Acessar o carrinho diretamente sem adicionar produto
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(3)

        # Verificar que o carrinho está vazio
        items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) == 0, f"Erro: Esperado carrinho vazio, mas encontrou {len(items)} item(ns)"

    def test_carrinho_com_produto_sem_remover(self):
        driver = self.driver

        # Já está na página de produtos (catálogo)

        # Adicionar um produto
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

        # Ir para o carrinho
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        # Não remover o produto, apenas verificar que está lá
        items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) == 1, f"Erro: Esperado 1 item no carrinho, mas encontrou {len(items)}"
        time.sleep(2)

        product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert product_name == "Sauce Labs Backpack", f"Produto incorreto no carrinho: {product_name}"
