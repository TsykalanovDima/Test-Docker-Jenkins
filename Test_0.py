import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
options = webdriver.ChromeOptions()

print(selenium.__version__)

@pytest.fixture
def driver():
    print('start')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--no-gpu')
    service = ChromeService(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()
    print("passed")

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    Login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'user-name'))
    )
    Login.send_keys('standard_user')

    Psw = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    Psw.send_keys('secret_sauce')

    assert "Swag Labs" in driver.title
    print("+")

def button_and_check(driver):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'login-button'))
    )
    button.click()
    try:
        test_text = driver.find_element(By.CLASS_NAME, 'app_logo').text
        assert test_text == 'Swag Labs', "False - "
        print("+")
    except Exception as e:
        print(" - ", e)
