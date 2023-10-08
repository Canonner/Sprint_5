from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators, RegisterPageLocators, AuthPageLocators
from data import CommonData


class TestRegistration:
    def test_registration_valid_data_successful_registration(self, driver):
        """
            Tests successful registration with valid data.
            Steps:
            1. Retrieve registration data from the CommonData module.
            2. Fill in the registration form with the name, login, and password.
            3. Click the register button.
            4. Wait for the account button on the main page to be visible and click it.
            5. Wait for the email input field on the authorization page to be visible.
            6. Fill in the authorization form with the login and password.
            7. Click the sign-in button.
            8. Assert that the place order button on the main page is visible.
        """
        data = CommonData.reg_data()
        name = data['name']
        login = data['login']
        password = data['password']

        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(RegisterPageLocators.REGISTER_BUTTON_REG))
        driver.find_element(*RegisterPageLocators.NAME_INPUT_FIELD_REG).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT_FIELD_REG).send_keys(login)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT_FIELD_REG).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON_REG).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.ACCOUNT_BUTTON_HEADER)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*AuthPageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(login)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(password)
        driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))

    def test_registration_invalid_password_error_received(self, driver):
        """
        Tests that an error message is displayed when registering with an invalid password.

        Steps:
        1. Retrieve registration data from the CommonData module.
        2. Fill in the registration form with the name, login, and invalid password.
        3. Click the register button.
        4. Assert that the incorrect password error message is displayed.
        """
        data = CommonData.reg_data()
        name = data['name']
        login = data['login']

        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(RegisterPageLocators.REGISTER_BUTTON_REG))
        driver.find_element(*RegisterPageLocators.NAME_INPUT_FIELD_REG).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT_FIELD_REG).send_keys(login)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT_FIELD_REG).send_keys(CommonData.invalid_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON_REG).click()
        assert driver.find_element(*RegisterPageLocators.INCORRECT_PASSWORD_ERROR_REG)
