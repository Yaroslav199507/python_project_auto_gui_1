import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Catalog_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    catalog_button = '//a[@data-meta-name="DesktopHeaderFixed__catalog-menu"]'
    smartphones = '//a[@data-meta-name="DesktopMenu__sub-category"]'
    cat_smartphones_word = '//h1[@class="elbnj820 eml1k9j0 app-catalog-kfo60a e1gjr6xo0"]'
    filter_self_pickup = '//div[@data-meta-value="Доступен самовывоз"]'
    filter_Apple = '//div[@data-meta-value="APPLE"]'
    product_1 = '(//a[@data-meta-name="Snippet__title"])[1]'
    select_product_1 = '(//button[@data-meta-name="Snippet__cart-button"])[1]'
    filter_Apple_word = '(//span[@class="e1ys5m360 e106ikdt0 app-catalog-rx1cfc e1gjr6xo0"])[2]'
    filter_self_pickup_word = '(//span[@class="e1ys5m360 e106ikdt0 app-catalog-rx1cfc e1gjr6xo0"])[1]'
    close_card_product = '//button[@data-meta-name="UpsaleBasket__close-popup"]'
    button_to_cart = '(//div[@data-meta-name="BasketButton"])[1]'
    cart_word = '//span[@class="e1ys5m360 e106ikdt0 css-8hy98m e1gjr6xo0"]'

    #Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones)))

    def get_cat_smart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cat_smartphones_word)))

    def get_filter_self_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_self_pickup)))

    def get_filter_Apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_Apple)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_filter_Apple_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_Apple_word)))

    def get_filter_self_pickup_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_self_pickup_word)))

    def get_button_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_to_cart)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    def get_close_card_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_card_product)))

    def get_close_card_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_card_product)))

    #Actions

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Переход в каталог товаров")

    def click_smartphones(self):
        self.get_smartphones().click()
        time.sleep(3)
        print("Выбор категории смартфоны")

    def click_filter_self_pickup(self):
        self.get_filter_self_pickup().click()
        print("Фильтр самовывоз")

    def click_filter_Apple(self):
        self.get_filter_Apple().click()
        print("Фильтр Apple")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        time.sleep(5)
        print("Выбран Продукт 1")

    def click_close_card_product(self):
        self.get_close_card_product().click()

    def click_button_to_cart(self):
        self.get_button_to_cart().click()
        print("Переход в корзину")

    def name_product_1(self):
        self.get_product_1().text


    #Methods
    def select_products(self):
        self.click_catalog_button()
        self.click_smartphones()
        self.assert_word(self.get_cat_smart_word(), "Смартфоны")
        self.scroll_down("600", "0")
        self.click_filter_self_pickup()
        self.scroll_down("1400", "0")
        self.click_filter_Apple()
        self.scroll_down("-300", "0")
        self.assert_word(self.get_filter_Apple_word(), "APPLE")
        self.assert_word(self.get_filter_self_pickup_word(), "Доступен самовывоз")
        self.scroll_down("300", "0")
        self.name_product_1()
        self.click_select_product_1()
        self.click_close_card_product()
        self.click_button_to_cart()
        self.assert_word(self.get_cart_word(), "Корзина")





