from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class TestSignIn:

    # проверка входа по кнопке «Войти в аккаунт» на главной
    def test_authorization_via_sign_in_account_button(self, driver):
        driver.find_element(*Locators.SIGN_IN_ACCOUNT_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_AUTH).send_keys('test_user_burgers123@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_AUTH).send_keys('123456')
        driver.find_element(*Locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

    # проверка входа через кнопку «Личный кабинет»
    def test_authorization_via_account_button(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_AUTH).send_keys('test_user_burgers123@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_AUTH).send_keys('123456')
        driver.find_element(*Locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

    # проверка входа через кнопку в форме регистрации
    def test_authorization_via_sign_in_register_button(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.SIGN_IN_BUTTON_REG)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_AUTH).send_keys('test_user_burgers123@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_AUTH).send_keys('123456')
        driver.find_element(*Locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

        # проверка входа через кнопку в форме восстановления пароля
    def test_authorization_via_sign_in_forgot_password_button(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.FORGOT_PASSWORD_BUTTON_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.SIGN_IN_BUTTON_FORGOT_PASSWORD)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_AUTH).send_keys('test_user_burgers123@ya.ru')
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_AUTH).send_keys('123456')
        driver.find_element(*Locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
