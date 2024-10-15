from selenium.webdriver.common.by import By


class LocatorsOrder:
    NEXT_BUTTON = By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM"
    INPUT_NAME = By.CSS_SELECTOR, "input[placeholder='* Имя']"
    INPUT_SURNAME = By.CSS_SELECTOR, "input[placeholder='* Фамилия']"
    INPUT_ADDRESS = By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"
    INPUT_METRO = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    INPUT_METRO_BUTTON = By.CSS_SELECTOR, "button[value='2']"
    INPUT_PHONE = By.CSS_SELECTOR, "input[placeholder = '* Телефон: на него позвонит курьер']"
    INPUT_DATE_QUESTION = By.CSS_SELECTOR, "input[placeholder = '* Когда привезти самокат']"
    INPUT_DATE = By.CSS_SELECTOR, "div[aria-label = 'Choose четверг, 31-е октября 2024 г.']"
    DROP_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-placeholder']"
    DROP_RENTAL_PERIOD_OPTION = By.XPATH, "//div[contains(text(), 'сутки')]"
    CHECKBOX_BLACK_SCOOTER = By.CSS_SELECTOR, "label[for='black']"
    INPUT_COMMENT = By.CSS_SELECTOR, "input[placeholder = 'Комментарий для курьера']"
    ORDER_BUTTON_ORDER_PAGE = By.CSS_SELECTOR, "button[class ='Button_Button__ra12g Button_Middle__1CSJM']"
    ONWARDS_BUTTON = By.XPATH, "//button[contains(text(),'Далее')]"
    YES_BUTTON_ORDER_PAGE = By.XPATH, "//button[contains(text(),'Да')]"
    TITLE_ORDER_PLACED = By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ"
    TITLE_ORDER = By.CSS_SELECTOR, ".Order_Header__BZXOb"
    SCOOTER_TITLE = By.CSS_SELECTOR, "img[alt='Scooter']"

