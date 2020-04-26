from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('link', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer5",
                                  "?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                  "?promo=offer8",
                                  "?promo=offer9"])

def test_guest_can_add_product_to_basket(browser,link):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
    page=ProductPage(browser,link)
    page.open()
    page.should_be_possible_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_correctly()

