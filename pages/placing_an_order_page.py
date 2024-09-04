
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    button_add_client = '(//button[@type="button"])[2]'
    first_name = '//input[@name="RecipientForm__first-name"]'
    last_name = '//input[@name="RecipientForm__last-name"]'
    phone = '//input[@placeholder="Телефон"]'
    button_create_client = '//button[@data-meta-name="RecipientForm__action-button"]'
    button_pickup_point = '(//button[@type="button"])[3]'
    button_add_pickup_point = '(//button[@class="css-jkwyhv e1k5z3pz0"])[1]'

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

    def get_button_add_pickup_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_pickup_point)))

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
        print('Клик "создать покупателя"')

    def click_button_pickup_point(self):
        self.get_button_pickup_point().click()
        print('Клик "перейти к выбору пункта самовывоза"')

    def click_button_add_pickup_point(self):
        self.get_button_add_pickup_point().click()
        print('Клик "выбрать пункт самовывоза"')


    #Methods
    def input_client_information(self):
        self.get_current_url()
        self.click_button_add_client()
        self.input_first_name("Ivan")
        self.input_last_name("Ivanov")
        self.input_phone("79270000000")
        self.click_button_create_client()
        self.click_button_pickup_point()
        # self.click_button_add_pickup_point()



