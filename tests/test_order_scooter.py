import allure
from locators.locators_main_page import LocatorsMain
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.description("Проверка возможности заказать самокат по верхней кнопке 'Заказать' с заполнением всех полей")
    @allure.title("Заказ самоката по верхней кнопке 'Заказать'")
    def test_make_an_order_for_top_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_main_cookie()
        main_page.click_on_order_top_button()
        order_page = OrderPage(driver)
        assert 'Заказ оформлен' in order_page.make_an_order_man_top_button()

    @allure.description("Проверка возможности заказать самокат по нижней кнопке 'Заказать' с заполнением всех полей")
    @allure.title("Заказ самоката по нижней кнопке 'Заказать'")
    def test_make_an_order_for_bot_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_main_cookie()
        main_page.scroll_to_element(LocatorsMain.POINT_FOUR)
        main_page.click_on_order_bot_button()
        order_page = OrderPage(driver)
        assert 'Заказ оформлен' in order_page.make_an_order_woman_bot_button()

