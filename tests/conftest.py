import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators, AuthPageLocators
from data import CommonData


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(CommonData.main_url)
    yield browser
    browser.quit()


@pytest.fixture
def sign_in(driver):
    driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT_FIELD_AUTH))
    driver.find_element(*AuthPageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
    driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON_AUTH).click()
