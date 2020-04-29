from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_products_in_basket()
        self.should_be_message_about_empty_basket()

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "There is product in basket, should not be."

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), "Message about empty basket is not presented"
        basket_message=self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET).text
        expected_basket_message = "Your basket is empty."
        assert expected_basket_message in basket_message, "Basket is not empty."