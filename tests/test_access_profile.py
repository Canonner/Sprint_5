from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators, ProfilePageLocators, FeedPageLocators


class TestAccessProfile:

    def test_access_to_profile_from_main(self, driver, sign_in):
        """Checks the transition to the Profile page from the Main page by clicking on the "Account" button."""
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(ProfilePageLocators.PROFILE_URL_ACCOUNT))

    def test_access_to_profile_from_feed(self, driver, sign_in):
        """Checks the transition to the Profile page from the Feed page by clicking on the "Account" button."""
        driver.find_element(*MainPageLocators.FEED_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(FeedPageLocators.FEED_HEADER))
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(ProfilePageLocators.PROFILE_URL_ACCOUNT))
