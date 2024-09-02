import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    button_go_to_checkout = '//span[text()="Перейти к оформлению"]'

    #Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_checkout)))


    #Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Переход к оформлению")


    #Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()