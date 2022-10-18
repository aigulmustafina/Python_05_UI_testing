import pytest
import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/ru/'

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу с товарами
@pytest.mark.smoke
def test_guest_can_go_to_catalogue(browser):
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # открывает страницу
    page.open_page()
    # проверяет, что на главной странице присутствует ссылка на страницу товаров
    page.should_be_link_to_product_page()
    # переходит на страницу с товарами
    page.go_to_product_page()

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу авторизации
@pytest.mark.regression
def test_guest_can_go_to_login_page(browser):
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # открывает страницу
    page.open_page()
    # переходит на страницу авторизации
    page.go_to_login_page()
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # проверяет, что текущая страница является страницей авторизации
    page.should_be_login_page()

# Тест проверяет, что пользователь может зарегистрироваться
def test_user_сan_autorize(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    # открывает страницу авторизации
    page.open_page()
    # регистрирует нового пользователя
    page.register_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
    # проверяет, что пользователь авторизован
    page.should_be_autorized_user()
