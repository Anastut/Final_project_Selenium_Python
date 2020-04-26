from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM=(By.CSS_SELECTOR,"#register_form")
    LOGIN_FORM=(By.CSS_SELECTOR,"#login_form")

class ProductPageLocators():
    ADD_TO_BASKET=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE=(By.CSS_SELECTOR,".price_color")
    PRODUCT=(By.CSS_SELECTOR,"div.product_main h1")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    MESSAGE_ABOUT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
