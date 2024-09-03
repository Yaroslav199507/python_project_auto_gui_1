
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.catalog_page import Catalog_page


def test_cancel_order():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    # options.add_experimental_option("detach", True)
    # options.add_argument("--headless")  #тест без открытия браузера
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start test 2")

    lp = Login_page(driver)
    lp.authorization()

