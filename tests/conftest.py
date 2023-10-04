import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators
import random as r


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window_size=1600,900")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def reg_data():
    name_seq = ['Ев', 'Ге', 'Ний', 'Во', 'Лк', 'Ов']
    name = f'{r.choice(name_seq)}'
    login = f'evgeniivolkov1{r.randint(100, 1000)}@ya.ru'
    pass_seq = ['able', 'baker', 'charlie', 'dog', 'easy', 'fox']
    password = f'{r.choice(pass_seq)}{r.randint(100, 1000)}'
    return {'name': name, 'login': login, 'password': password}


@pytest.fixture
def sign_in(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.EMAIL_INPUT_FIELD_AUTH))
    driver.find_element(*Locators.EMAIL_INPUT_FIELD_AUTH).send_keys('test_user_burgers123@ya.ru')
    driver.find_element(*Locators.PASSWORD_INPUT_FIELD_AUTH).send_keys('123456')
    driver.find_element(*Locators.SIGN_IN_BUTTON_AUTH).click()
