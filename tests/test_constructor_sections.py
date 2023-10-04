from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators

class TestConstructorSections:

    def test_constructor_section_buns(self, driver):
        element = driver.find_element(*Locators.FILLINGS_HEADER)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*Locators.BUNS_SPAN).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(Locators.BUNS_HEADER))


    def test_constructor_section_sauces(self, driver):
        driver.find_element(*Locators.SAUCES_SPAN).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(Locators.SAUCES_HEADER))


    def test_constructor_section_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS_SPAN).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(Locators.FILLINGS_HEADER))