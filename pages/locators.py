from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "#id_login-redirect_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.ID, "add_to_basket_form")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    ADDED_TO_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
