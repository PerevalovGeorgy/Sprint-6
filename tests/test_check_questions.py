import allure
import pytest
from pages.main_page import MainPage
from data import QuestionAnswerLict


class TestQuestionOnMainPage:

    @allure.description("При прохождении теста выполняется переход на главную, отжим кнопки кук, скрол до последнего вопроса и проверка всех ответов")
    @allure.title("Проверка ответов на 'Вопросы о важном' на главной странице")
    @pytest.mark.parametrize('num,result', QuestionAnswerLict.lict)
    def test_check_all_questions_and_answers(self,  driver, num, result):
        main_page = MainPage(driver)
        main_page.click_on_main_cookie()
        assert main_page.check_the_text_of_the_question(num) == result
