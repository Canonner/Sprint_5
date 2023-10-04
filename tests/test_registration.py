from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class TestRegistration:
    def test_registration_valid_data_successful_registration(self, driver, reg_data):
        # имя, логин и пароль из фикстуры для регистрации
        name = reg_data['name']
        login = reg_data['login']
        password = reg_data['password']

        # блок перехода с главной страницы сайта через форму авторизации к форме регистрации
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.REGISTER_BUTTON_REG))

        # блок ввода данных для регистрации нового пользователя
        driver.find_element(*Locators.NAME_INPUT_FIELD_REG).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_REG).send_keys(login)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_REG).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON_REG).click()

        # блок проверки регистрации - переход в форму авторизации, ввод почты и пароля и проверка
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.ACCOUNT_BUTTON_HEADER)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_AUTH).send_keys(login)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_AUTH).send_keys(password)
        driver.find_element(*Locators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))

    def test_registration_invalid_password_error_received(self, driver, reg_data):
        # имя, логин и пароль из фикстуры для регистрации
        name = reg_data['name']
        login = reg_data['login']
        invalid_password = '12345'

        # блок перехода с главной страницы сайта через форму авторизации к форме регистрации
        driver.find_element(*Locators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(Locators.REGISTER_BUTTON_REG))

        # блок ввода данных для регистрации нового пользователя
        driver.find_element(*Locators.NAME_INPUT_FIELD_REG).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_FIELD_REG).send_keys(login)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD_REG).send_keys(invalid_password)
        driver.find_element(*Locators.REGISTER_BUTTON_REG).click()

        # блок проверки появления ошибки
        assert driver.find_element(*Locators.INCORRECT_PASSWORD_ERROR_REG)
