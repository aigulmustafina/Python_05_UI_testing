import pytest
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
link = 'http://selenium1py.pythonanywhere.com/ru/'

# class TestMainPage():

    # @pytest.mark.open_page
    # @pytest.mark.smoke
def test_guest_can_go_to_catalogue(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_view_products()
    page.go_to_catalogue()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    time.sleep(2)
    page = LoginPage(browser, link)
    page.should_be_login_page()

def test_user_should_be_autorized(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open_page()
    page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
    page.should_be_autorized_user()



