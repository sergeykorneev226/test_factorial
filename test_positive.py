import pytest
import math
import decimal
from pages.locators import MainPageLocators
from selenium import webdriver


@pytest.mark.parametrize('numbers', [0, 1, 169, 170])
def test_positive_factorial(numbers):
    browser = webdriver.Firefox()
    url = "https://qa-test.emcd.io"
    browser.get(url)
    input_field = browser.find_element(*MainPageLocators.INPUT_FIELD)
    input_field.clear()
    input_field.send_keys(numbers)
    button = browser.find_element(*MainPageLocators.BUTTON)
    button.click()
    result = browser.find_element(*MainPageLocators.RESULT)
    answer = result.text
    number_answer = answer.split(": ")[-1]
    assert float(number_answer) == float(format(decimal.Decimal(math.factorial(numbers)), '.15e')), "Factorial calculator is not working correctly"
    browser.quit()
