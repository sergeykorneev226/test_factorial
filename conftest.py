import pytest
from selenium import webdriver


# Фикстура, подготавливающая и закрывающая окружение
@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Firefox
    yield browser
    print("\nquit browser..")
    browser.quit()
