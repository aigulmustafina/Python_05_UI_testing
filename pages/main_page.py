from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_link_to_product_page(self):
        assert self.element_is_present(*MainPageLocators.LINK_TO_PRODUCT_PAGE)

    def go_to_product_page(self):
        self.browser.find_element(*MainPageLocators.LINK_TO_PRODUCT_PAGE).click()

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()



