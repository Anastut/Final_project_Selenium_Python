from .locators import MainPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    def go_to_login_page(self):
        self.should_be_login_link.click()
