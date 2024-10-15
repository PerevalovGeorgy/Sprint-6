from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def base_click_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_in_element(self, locator, text):
        self.wait_element_and_find_element(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.wait_element_and_find_element(locator).text

    def format_locators(self, locator_1, num):
        metod, locator = locator_1
        locator = locator.format(num)
        return metod, locator

    def base_scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def base_get_element_attribute(self, locator, atr):
        return self.wait_element_and_find_element(locator).get_attribute(atr)

    def base_switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

