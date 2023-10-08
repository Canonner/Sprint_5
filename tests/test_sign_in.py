from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators, AuthPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from data import CommonData


class TestSignIn:

    def test_authorization_via_sign_in_account_button(self, driver):
        """Test authorization using the 'Sign In Account' button on the Main page."""
        driver.find_element(*MainPageLocators.SIGN_IN_ACCOUNT_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*AuthPageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
        driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))

    def test_authorization_via_account_button(self, driver):
        """Test authorization using the 'Account' button."""
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*AuthPageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
        driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))

    def test_authorization_via_sign_in_register_button(self, driver):
        """Test authorization using the 'Sign In' button on the registration form."""
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(RegisterPageLocators.SIGN_IN_BUTTON_REG)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*AuthPageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
        driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))

    def test_authorization_via_sign_in_forgot_password_button(self, driver):
        """Test authorization using the 'Sign In' button on the forgot password form."""
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON_HEADER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.FORGOT_PASSWORD_BUTTON_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(ForgotPasswordPageLocators.SIGN_IN_BUTTON_FORGOT_PASSWORD)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*AuthPageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
        driver.find_element(*AuthPageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
