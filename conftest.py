import pytest
from data import TestUrl
from selenium import webdriver
from locators.locators_main_page import LocatorsMain
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(TestUrl.url_main_page)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LocatorsMain.TITLE_MAIN))
    yield driver
    driver.quit()

