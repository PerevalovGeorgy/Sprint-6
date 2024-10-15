import allure
from locators.locators_main_page import LocatorsMain
from locators.locators_order_page import LocatorsOrder
from locators.locators_dzen_page import LocatorsDzen
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.dzen_page import DzenPage


class TestClickTitle:

    @allure.description("При прохождении теста выполняется нажатие кнопки кук, переход на страницу заказа и возврат на гланую по клику на надпись 'Самокат'")
    @allure.title("Переход по надписи 'Самокат'")
    def test_click_on_scooter_title(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_main_cookie()
        main_page.click_on_order_top_button()
        order_page = OrderPage(driver)
        order_page.click_element(LocatorsOrder.SCOOTER_TITLE)
        element_atr = main_page.get_element_attribute(LocatorsMain.SCOOTER_TITLE, "alt")
        assert 'Scooter' in element_atr

    @allure.description("При прохождении теста выполняется нажатие кнопки кук, переход на страницу Дзена с проверкой появления поиска")
    @allure.title("Переход по надписи 'Дзен'")
    def test_click_on_yandex_title(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_main_cookie()
        main_page.click_on_element(LocatorsMain.LOGO_YANDEX)
        main_page.base_switch_window()
        dzen_page = DzenPage(driver)
        assert 'Найти' in dzen_page.get_text_from_element(LocatorsDzen.SEARCH_BAR)

