import allure

from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMain


class MainPage(BasePage):
    @allure.step("Кликаем на верхнюю кнопку 'Заказать'")
    def click_on_order_top_button(self):
        self.base_click_element(LocatorsMain.ORDER_BUTTON_ON_TOP)

    @allure.step("Кликаем на нижнюю кнопку 'Заказать'")
    def click_on_order_bot_button(self):
        self.base_click_element(LocatorsMain.ORDER_BUTTON_ON_BOTTOM)

    @allure.step("Кликаем на выбранный элемент")
    def click_on_element(self, locator):
        self.base_click_element(locator)

    @allure.step("Получение текста ответа на соответствующий вопрос")
    def check_the_text_of_the_question(self, num):
        locator_q_format = self.format_locators(LocatorsMain.QUESTION_0, num)
        locator_a_format = self.format_locators(LocatorsMain.ANSWER_0, num)
        self.base_scroll_to_element(LocatorsMain.QUESTION_7)
        self.base_click_element(locator_q_format)
        return self.get_text_from_element(locator_a_format)

    @allure.step("Кликаем на кнопку приема куки")
    def click_on_main_cookie(self):
        self.base_click_element(LocatorsMain.COOKIE_BUTTON)

    @allure.step("Скролим до нужного элемента")
    def scroll_to_element(self, locator):
        self.base_scroll_to_element(locator)

    @allure.step("Получаем значение отрибута")
    def get_element_attribute(self, locator, atr):
        return self.base_get_element_attribute(locator, atr)

    @allure.step("Переходим на последнюю вкладку")
    def switch_window(self):
        self.base_switch_window()

