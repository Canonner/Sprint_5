from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class TestFromProfileToConstructor:

    # проверка перехода из Личного кабинета в Конструктор по клику на кнопку «Конструктор»
    def test_click_from_profile_on_constructor(self, driver, sign_in):
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PROFILE_URL_ACCOUNT))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.COMPILE_BURGER_HEADER))

    # проверка перехода из Личного кабинета в Конструктор по клику на логотип Stellar Burgers
    def test_click_from_profile_on_logo_burgers(self, driver, sign_in):
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PROFILE_URL_ACCOUNT))
        driver.find_element(*Locators.LOGO_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.COMPILE_BURGER_HEADER))
