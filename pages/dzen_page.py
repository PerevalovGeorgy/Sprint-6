import allure
from pages.base_page import BasePage


class DzenPage(BasePage):

    @allure.step("Получаем значение отрибута")
    def get_element_attribute(self, locator):
        return self.get_text_from_element(locator)

