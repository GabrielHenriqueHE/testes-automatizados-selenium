from selenium import webdriver


class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome()
