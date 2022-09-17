from selenium.webdriver.common.by import By


class MainPageLocators():
    URL = ("https://qa-test.emcd.io")
    INPUT_FIELD = (By.CSS_SELECTOR, "#number")
    BUTTON = (By.CSS_SELECTOR, "#getFactorial")
    RESULT = (By.CSS_SELECTOR, "#resultDiv")
