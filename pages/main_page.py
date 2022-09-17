from base_page import BasePage
from locators import MainPageLocators
import pytest
import math
import decimal


class MainPage(BasePage):
    @pytest.mark.parametrize('numbers', [0, 1, 169, 170])
    def test_positive_factorial(self, numbers):
        browser = self.webdriver.Firefox()
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
        assert float(number_answer) == float(
            format(decimal.Decimal(math.factorial(numbers)), '.15e')), "Factorial calculator is not working correctly"
        browser.quit()