from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_BUSKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_ADD_BUSKET = (By.TAG_NAME, "h1")
    PRODUCT_IN_BUSKET =(By.LINK_TEXT, "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/")

class LoginPageLocators():
    FORM_REG = (By.CSS_SELECTOR, "#register_form")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    BTN_BASKET_SHAPKA = (By.CLASS_NAME, "btn-group a")
    BTN_PROCEED_CHECKOUT = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-block")
    TXT_BUSKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")