import allure
import pytest
from selenium import webdriver

from pages.home_page import HomePageScooter


class TestFaq:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка соответствия ответов вопросам в секции "Вопросы о важном"')
    @allure.description(
        'В тесте проверяется порядок вопросов, содержание вопросов и ответов и соответствие ответов вопросам.')
    @pytest.mark.parametrize('option_index', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_answers_matching_questions_in_faq_section(self, option_index):
        home_page = HomePageScooter(self.driver)

        home_page.open_home_page_by_direct_url()

        home_page.click_on_question_by_index(option_index)

        home_page.verify_faq_answer_expanded(option_index)
        home_page.verify_faq_answer_by_question_index(option_index)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
