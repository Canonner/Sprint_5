from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators, ProfilePageLocators, AuthPageLocators


def test_exit_from_account(driver, sign_in):
    driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON_ACCOUNT)).click()
    assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.SIGN_IN_BUTTON_AUTH))
