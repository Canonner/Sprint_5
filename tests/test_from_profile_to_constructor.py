from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators, ProfilePageLocators


class TestFromProfileToConstructor:

    def test_click_from_profile_on_constructor(self, driver, sign_in):
        """Checks the transition from the Profile page to the Constructor by clicking on the "Constructor" button."""
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(ProfilePageLocators.PROFILE_URL_ACCOUNT))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.COMPILE_BURGER_HEADER))

    def test_click_from_profile_on_logo_burgers(self, driver, sign_in):
        """Checks the transition from the Profile page to the Constructor by clicking on the Stellar Burgers logo."""
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(ProfilePageLocators.PROFILE_URL_ACCOUNT))
        driver.find_element(*ProfilePageLocators.LOGO_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.COMPILE_BURGER_HEADER))
