from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import faker

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page=ProductPage(browser,link)
    page.open()
    page.should_be_possible_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_correctly()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link= "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page=BasketPage(browser,link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()
    page.should_be_empty_basket()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link="http://selenium1py.pythonanywhere.com/accounts/login/"
        f=faker.Faker()
        email=f.email()
        password="@1234Test"
        self.page = LoginPage(browser=browser, url=link)
        self.page.open()
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_possible_add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_added_correctly()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_message_about_adding()


