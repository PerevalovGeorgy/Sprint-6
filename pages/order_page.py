import allure
from pages.base_page import BasePage
from locators.locators_order_page import LocatorsOrder
from data import UserDataMan, UserDataWoman


class OrderPage(BasePage):

    @allure.step("Кликаем на выбранный элемент")
    def click_element(self, locator):
        self.base_click_element(locator)
    @allure.step("Заказ самоката с заполнением всех полей под пользователем мужчиной")
    def make_an_order_man_top_button(self):
        self.wait_element_and_find_element(LocatorsOrder.TITLE_ORDER)
        self.add_text_in_element(LocatorsOrder.INPUT_NAME, UserDataMan.name)
        self.add_text_in_element(LocatorsOrder.INPUT_SURNAME, UserDataMan.surname)
        self.add_text_in_element(LocatorsOrder.INPUT_ADDRESS, UserDataMan.address)
        self.base_click_element(LocatorsOrder.INPUT_METRO)
        self.base_click_element(LocatorsOrder.INPUT_METRO_BUTTON)
        self.add_text_in_element(LocatorsOrder.INPUT_PHONE, UserDataMan.telephone)
        self.base_click_element(LocatorsOrder.ONWARDS_BUTTON)
        self.wait_element_and_find_element(LocatorsOrder.TITLE_ORDER)
        self.base_click_element(LocatorsOrder.INPUT_DATE_QUESTION)
        self.base_click_element(LocatorsOrder.INPUT_DATE)
        self.base_click_element(LocatorsOrder.DROP_RENTAL_PERIOD)
        self.base_click_element(LocatorsOrder.DROP_RENTAL_PERIOD_OPTION)
        self.base_click_element(LocatorsOrder.CHECKBOX_BLACK_SCOOTER)
        self.base_click_element(LocatorsOrder.ORDER_BUTTON_ORDER_PAGE)
        self.wait_element_and_find_element(LocatorsOrder.TITLE_ORDER_PLACED)
        self.base_click_element(LocatorsOrder.YES_BUTTON_ORDER_PAGE)
        self.wait_element_and_find_element(LocatorsOrder.TITLE_ORDER_PLACED)
        return self.get_text_from_element(LocatorsOrder.TITLE_ORDER_PLACED)

    @allure.step("Заказ самоката с заполнением всех полей под пользователем женщиной")
    def make_an_order_woman_bot_button(self):
        self.wait_element_and_find_element(LocatorsOrder.TITLE_ORDER)
        self.add_text_in_element(LocatorsOrder.INPUT_NAME, UserDataWoman.name)
        self.add_text_in_element(LocatorsOrder.INPUT_SURNAME, UserDataWoman.surname)
        self.add_text_in_element(LocatorsOrder.INPUT_ADDRESS, UserDataWoman.address)
        self.base_click_element(LocatorsOrder.INPUT_METRO)
        self.base_click_element(LocatorsOrder.INPUT_METRO_BUTTON)
        self.add_text_in_element(LocatorsOrder.INPUT_PHONE, UserDataWoman.telephone)
        self.base_click_element(LocatorsOrder.ONWARDS_BUTTON)
        self.wait_element_and_find_element(LocatorsOrder.TITLE_ORDER)
        self.base_click_element(LocatorsOrder.INPUT_DATE_QUESTION)
        self.base_click_element(LocatorsOrder.INPUT_DATE)
        self.base_click_element(LocatorsOrder.DROP_RENTAL_PERIOD)
        self.base_click_element(LocatorsOrder.DROP_RENTAL_PERIOD_OPTION)
        self.base_click_element(LocatorsOrder.CHECKBOX_BLACK_SCOOTER)
        self.base_click_element(LocatorsOrder.ORDER_BUTTON_ORDER_PAGE)
        self.wait_element_and_find_element(LocatorsOrder.TITLE_ORDER_PLACED)
        self.base_click_element(LocatorsOrder.YES_BUTTON_ORDER_PAGE)
        self.wait_element_and_find_element(LocatorsOrder.TITLE_ORDER_PLACED)
        return self.get_text_from_element(LocatorsOrder.TITLE_ORDER_PLACED)

