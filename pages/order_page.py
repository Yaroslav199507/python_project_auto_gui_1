import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    button_1_go_to_order_page = '(//div[@role="button"])[1]'
    button_2_go_to_order_page = '//a[@data-meta-name="ProfileMenu_Item_Заказы"]'
    word_order = '//h2[@class="e114sczy0 eml1k9j0 css-qy8up7 e1gjr6xo0"]'
    button_cancel_order = '(//button[@class="e4uhfkv0 css-pjyyz3 e4mggex0"])[1]'
    cancel_reason = '(//label[@class="e1f9rbm30 e36y7rh0 css-15fscxw e3uwebf0"])[2]'
    button_cancel_finish = '(//button[@type="submit"])[3]'
    word_cancelled = '(//span[@class="e9prjkn0 e1b1w42r0 e106ikdt0 css-gncu7c e1gjr6xo0"])[1]'


    #Getters

    def get_button_1_go_to_order_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_1_go_to_order_page)))

    def get_button_2_go_to_order_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_2_go_to_order_page)))

    def get_word_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_order)))

    def get_button_cancel_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cancel_order)))

    def get_cancel_reason(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel_reason)))

    def get_button_cancel_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cancel_finish)))

    def get_word_cancelled(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_cancelled)))


    #Actions


    def click_button_1_go_to_order_page(self):
        self.get_button_1_go_to_order_page().click()
        print('Переход к кнопке "Заказы"')

    def click_button_2_go_to_order_page(self):
        self.get_button_2_go_to_order_page().click()
        print('Переход в раздел "Заказы"')

    def click_button_cancel_order(self):
        self.get_button_cancel_order().click()
        print('Переход к отмене заказа')

    def click_cancel_reason(self):
        self.get_cancel_reason().click()
        print('Выбор причины отмены')

    def click_button_cancel_finish(self):
        self.get_button_cancel_finish().click()
        print('Отмена заказа - Да')


    #Methods
    def go_to_order_cancel(self):
        self.click_button_1_go_to_order_page()
        self.click_button_2_go_to_order_page()
        self.assert_word(self.get_word_order(), "Заказы")
        self.click_button_cancel_order()
        self.click_cancel_reason()
        self.click_button_cancel_finish()
        self.assert_word(self.get_word_cancelled(), "Отменён")
