from .locators import LoginPageLocators
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.element_is_present(*LoginPageLocators.REGISTER_FORM)

    def register_user(self, email='email', password = 'password'):
        email_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        password_input.send_keys(password)
        password_conf_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        password_conf_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()

