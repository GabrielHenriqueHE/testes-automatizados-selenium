# test_login_saucedemo.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

# URL base do sistema
URL = "https://www.saucedemo.com/v1/"
USUARIO_VALIDO = "standard_user"
SENHA_VALIDA = "secret_sauce"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    time.sleep(2)  # Espera após abrir o navegador
    yield driver
    time.sleep(2)  # Espera antes de fechar o navegador
    driver.quit()

def realizar_login(driver, username, password):
    time.sleep(1)  # Espera antes de começar a digitar
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Espera para carregar o resultado do login

def test_login_com_credenciais_validas(driver):
    realizar_login(driver, USUARIO_VALIDO, SENHA_VALIDA)
    assert "inventory" in driver.current_url, "Login falhou com credenciais válidas"
    time.sleep(2)

def test_login_com_usuario_incorreto(driver):
    realizar_login(driver, "usuario_errado", SENHA_VALIDA)
    mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Username and password do not match" in mensagem_erro or "do not match" in mensagem_erro
    time.sleep(2)

def test_login_com_senha_incorreta(driver):
    realizar_login(driver, USUARIO_VALIDO, "senha_errada")
    mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Username and password do not match" in mensagem_erro or "do not match" in mensagem_erro
    time.sleep(2)

def test_login_com_usuario_e_senha_incorretos(driver):
    realizar_login(driver, "usuario_errado", "senha_errada")
    mensagem_erro = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Username and password do not match" in mensagem_erro or "do not match" in mensagem_erro
    time.sleep(2)
