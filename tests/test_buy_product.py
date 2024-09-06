
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.catalog_page import CatalogPage
from pages.order_page import OrderPage
from pages.placing_an_order_page import ClientInformationPage


def test_buy_product_1(set_up):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=Service())


    print("Start test 1")

    lp = LoginPage(driver)
    lp.authorization()

    cat = CatalogPage(driver)
    cat.select_products()

    cp = CartPage(driver)
    cp.product_confirmation()

    pop = ClientInformationPage(driver)
    pop.input_client_information()

    print("Finish Test 1")

def test_cancel_order(set_up):
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start test 2")

    lp = LoginPage(driver)
    lp.authorization()

    op = OrderPage(driver)
    op.go_to_order_cancel()

    print("Finish Test 2")



