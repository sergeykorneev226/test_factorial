from pages.main_page import MainPage


class TestMainPage:
    def test_function(self, browser):
        page = MainPage()
        page.open()
        page.test_positive_factorial()
