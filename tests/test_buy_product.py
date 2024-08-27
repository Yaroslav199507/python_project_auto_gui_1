
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login_page
from pages.catalog import Catalog_page


def test_select_product_1():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    # options.add_experimental_option("detach", True)
    # options.add_argument("--headless")  #тест без открытия браузера
    driver = webdriver.Chrome(options=options, service=Service())

    print("Start test 1")

    lp = Login_page(driver)
    lp.authorization()

    cat = Catalog_page(driver)
    cat.select_products()

    time.sleep(5)