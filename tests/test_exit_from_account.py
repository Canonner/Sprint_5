from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


def test_exit_from_account(driver, sign_in):
    driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.EXIT_BUTTON_ACCOUNT)).click()
    assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.SIGN_IN_BUTTON_AUTH))
