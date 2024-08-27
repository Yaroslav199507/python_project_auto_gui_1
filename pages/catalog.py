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
    select_product_1 = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/button/span/span/svg'
    filter_Apple_word = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[1]/div[1]/div/div[4]/div/button/span[1]'
    filter_self_pickup_word = '//*[@id="__next"]/div/main/section/div[2]/div/div/section/div[2]/div[1]/div[1]/div/div[2]/div/button/span[1]'


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
        print("Выбран Продукт 1")


    #Methods
    def select_products(self):
        self.click_catalog_button()
        self.click_smartphones()
        self.assert_word(self.get_cat_smart_word(), "Смартфоны")
        self.scroll_down("600", "0")
        self.click_filter_self_pickup()
        self.scroll_down("1400", "0")
        self.click_filter_Apple()
        time.sleep(5)
        self.scroll_down("-300", "0")
        time.sleep(5)
        # self.click_select_product_1()
        self.assert_word(self.get_filter_Apple_word(), "APPLE")
        self.assert_word(self.get_filter_self_pickup_word(), "Доступен самовывоз")






