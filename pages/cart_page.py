import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    button_go_to_checkout = '//span[text()="Перейти к оформлению"]'
    product_1_cart_price = '(//span[@data-meta-is-total="notTotal"])[15]'
    product_1_price_confirmation_page = '(//span[@data-meta-is-total="total"])[3]'
    confirmation_page_word = '//span[@class="e1ys5m360 e106ikdt0 css-p2oaao e1gjr6xo0"]'
    

    #Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_checkout)))

    def get_product_1_cart_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_cart_price)))

    def get_product_1_price_confirmation_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_price_confirmation_page)))

    def get_confirmation_page_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmation_page_word)))


    #Actions

    def product_cart_price(self):
        price_p1 = self.get_product_1_cart_price().text
        with open("C://Users//davyd//PycharmProjects//new_main_project//doc//price_product.txt", "w", encoding='utf-8') as files:
            files.write(price_p1)

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Переход к оформлению")

    def assert_price(self):
        file = open("C://Users//davyd//PycharmProjects//new_main_project//doc//price_product.txt", "r", encoding='utf-8')
        price = file.read()
        assert price == self.get_product_1_price_confirmation_page().text
        print("Цена продукта из корзины соответствует цене на стадии оформления!")


    #Methods
    def product_confirmation(self):
        self.get_current_url()
        self.product_cart_price()
        self.click_checkout_button()
        self.assert_word(self.get_confirmation_page_word(), "Оформление заказа")
        self.assert_price()
