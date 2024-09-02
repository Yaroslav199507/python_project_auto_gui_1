import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):

    url = "https://www.citilink.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    login_form_popup = "//div[@data-meta-name='UserButtonContainer']"
    user_mail = "//input[@name='login']"
    password = "//input[@name='pass']"
    button_login = "//button[@class='e4uhfkv0 css-1nvnwij e4mggex0']"
    main_word = "//span[@class='en3k2720 e106ikdt0 css-1y9ljh1 e1gjr6xo0']"

    #Getters

    def get_login_form_popup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_form_popup)))

    def get_user_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.main_word)))



    #Actions

    def click_login_form_popup(self):
        self.get_login_form_popup().click()
        print("Click Popup Login")

    def input_user_mail(self, user_mail):
        self.get_user_mail().send_keys(user_mail)
        print("input Login")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input Password")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click Login")


    #Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_form_popup()
        self.input_user_mail("shestakov0907@gmail.com")
        self.input_password("Ehurig3535")
        self.click_button_login()
        self.assert_word(self.get_main_word(), "Ярослав")