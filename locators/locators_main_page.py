from selenium.webdriver.common.by import By


class LocatorsMain:
    ORDER_BUTTON_ON_TOP = By.CSS_SELECTOR, "button[class='Button_Button__ra12g']"
    ORDER_BUTTON_ON_BOTTOM = By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button"
    ORDER_STATUS_BUTTON = By.CSS_SELECTOR, "// button[contains(text(), 'Статус заказа')]"
    SCOOTER_TITLE = By.CSS_SELECTOR, "img[alt='Scooter']"
    POINT_FOUR = By.CSS_SELECTOR, ".Home_StatusCircle__3_aTp.Home_Lineless__2-Rxp"
    QUESTION_0 = By.CSS_SELECTOR, "#accordion__heading-{}"
    QUESTION_7 = By.CSS_SELECTOR, "#accordion__heading-7"
    ANSWER_0 = By.CSS_SELECTOR, "div[id='accordion__panel-{}'] p"
    COOKIE_BUTTON = By.CSS_SELECTOR, "button[class='App_CookieButton__3cvqF']"
    TITLE_MAIN = By.CSS_SELECTOR, ".Home_Header__iJKdX"
    SCOOTER_IMG = By.CSS_SELECTOR, "img[src='/assets/scooter.png']"
    LOGO_YANDEX = By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI"

