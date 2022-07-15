import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.loginpage import LoginPage
import json

# Start the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Takes a file object and returns the json object.
f = open("data/datos.json")
data = json.load(f)

def test_loginOrange():
    login_page = LoginPage(driver)
    login_page.enter_login(data['user'], data['password'])
    assert login_page.validate_welcome().is_displayed()
    f.close()
    driver.close()
    driver.quit()


