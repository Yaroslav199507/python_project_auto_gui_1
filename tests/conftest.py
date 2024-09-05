import pytest
from selenium import webdriver

@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")
