from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON=(By.CSS_SELECTOR,".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_ABOUT_EMPTY_BASKET=(By.CSS_SELECTOR,"#content_inner")
    BASKET_ITEM=(By.CSS_SELECTOR,".basket-items")

class MainPageLocators():
    pass

class LoginPageLocators():
    REGISTER_FORM=(By.CSS_SELECTOR,"#register_form")
    LOGIN_FORM=(By.CSS_SELECTOR,"#login_form")
    EMAIL_FIELD=(By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_FIELD=(By.CSS_SELECTOR,"#id_registration-password1")
    PASSWORD_CHECK_FIELD=(By.CSS_SELECTOR,"#id_registration-password2")
    REGISTER_BUTTON=(By.NAME,"registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET=(By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE=(By.CSS_SELECTOR,".price_color")
    PRODUCT=(By.CSS_SELECTOR,"div.product_main h1")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    MESSAGE_ABOUT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


    
    
