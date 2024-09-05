import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class ClientInformationPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    button_add_client = '(//button[@type="button"])[2]'
    first_name = '//input[@name="RecipientForm__first-name"]'
    last_name = '//input[@name="RecipientForm__last-name"]'
    phone = '//input[@placeholder="Телефон"]'
    button_create_client = '//button[@data-meta-name="RecipientForm__action-button"]'
    button_pickup_point = '//*[@id="__next"]/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div/div[3]/div[2]/button'
    word_pickup_point = '//h3[@class="e114sczy0 eml1k9j0 css-5n8md8 e1gjr6xo0"]'
    button_add_pickup_point = '//*[@id="__next"]/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/button'
    payment_method_cash = '//*[@id="__next"]/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div/div[2]/div/div/div[1]/div/div[2]/label[2]/span/span[2]/span'
    button_order_confirm = '//*[@id="__next"]/div/div[2]/div/div/div/div/div[1]/div[4]/div/div[2]/div/div/div[3]/div/div[3]/button/span'
    word_order_placed = '//span[@class="e1ys5m360 e106ikdt0 css-8hy98m e1gjr6xo0"]'

    #Getters

    def get_button_add_client(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_client)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_button_create_client(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_create_client)))

    def get_button_pickup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_pickup_point)))

    def get_word_pickup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_pickup_point)))

    def get_button_add_pickup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_pickup_point)))

    def get_payment_method_cash(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method_cash)))

    def get_button_order_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_order_confirm)))

    def get_word_order_placed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_order_placed)))


    #Actions

    def click_button_add_client(self):
        self.get_button_add_client().click()
        print("Открытие формы добавления получателя")
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Ввод имени покупателя")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Ввод фамилии покупателя")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Ввод телефона покупателя")

    def click_button_create_client(self):
        self.get_button_create_client().click()
        time.sleep(3)
        print('Клик "создать покупателя"')

    def click_button_pickup_point(self):
        self.get_button_pickup_point().click()
        print('Клик "перейти к выбору пункта самовывоза"')

    def click_button_add_pickup_point(self):
        self.get_button_add_pickup_point().click()
        print('Клик "выбрать пункт самовывоза"')

    def click_payment_method_cash(self):
        self.get_payment_method_cash().click()
        print('Способ оплаты - наличными')

    def click_button_order_confirm(self):
        self.get_button_order_confirm().click()
        print('Клик "Оформить заказ"')


    #Methods
    def input_client_information(self):
        self.get_current_url()
        self.click_button_add_client()
        self.input_first_name("Ivan")
        self.input_last_name("Ivanov")
        self.input_phone("79270000000")
        self.click_button_create_client()
        self.click_button_pickup_point()
        self.assert_word(self.get_word_pickup_point(), 'Выберите магазин или пункт выдачи')
        self.click_button_add_pickup_point()
        self.scroll("700", "0")
        self.click_payment_method_cash()
        self.click_button_order_confirm()
        self.assert_word(self.get_word_order_placed(), "Заказ успешно создан!")
        self.screenshot()





