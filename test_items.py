from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestProductPage:
    def test_button_add_to_basket_exist_on_page(self, browser):
        browser.get(link)
        time.sleep(5)
        button = browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button')
        assert button, 'button not found'
