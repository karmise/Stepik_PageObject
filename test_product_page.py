from pages.product_page import ProductPage
import time


basket_page = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, basket_page)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.basket_should_be()
    time.sleep(5)
    pass
