from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_to_basket(self):
        add = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add.click()

    def basket_should_be(self):
        product = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET)
        product_text = product.text
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_text = name.text
        assert product_text == name_text, f"{product_text}!={name_text}"
