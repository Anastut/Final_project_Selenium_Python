from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def should_be_possible_add_to_basket(self):
        self.should_be_add_to_basket()
        self.add_to_basket()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button add to basket is not presented"

    def add_to_basket(self):
        button=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_be_added_correctly(self):
        self.should_be_message_about_adding()
        self.should_be_message_about_price()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Messsage about adding is not presented"
        product_name=self.browser.find_element(*ProductPageLocators.PRODUCT).text
        adding_message= self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        expected_adding_message= f"{product_name} has been added to your basket."
        assert  expected_adding_message == adding_message, "Added product with incorrect name"

    def should_be_message_about_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_PRICE), "Message about price is not presented"
        price=self.browser.find_element(*ProductPageLocators.PRICE).text
        price_message=self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_PRICE).text
        assert  price in price_message, "Added product with incorrect price"

    def should_not_be_message_about_adding(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is not disappeared, but should be"







