from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class TestAccessProfile:

    # проверка перехода в Личный кабинет с главной страницы по клику на кнопку «Личный кабинет»
    def test_access_to_profile_from_main(self, driver, sign_in):
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PROFILE_URL_ACCOUNT))

    # проверка перехода в Личный кабинет из ленты заказов по клику на кнопку «Личный кабинет»
    def test_access_to_profile_from_feed(self, driver, sign_in):
        driver.find_element(*Locators.FEED_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.FEED_HEADER))
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PROFILE_URL_ACCOUNT))
