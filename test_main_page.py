from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
login_page = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_should_be_login_url(browser):
    page = LoginPage(browser, login_page)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    page = LoginPage(browser, login_page)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    page = LoginPage(browser, login_page)
    page.open()
    page.should_be_register_form()
