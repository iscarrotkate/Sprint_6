import allure
import pytest
from selenium import webdriver
from helpers.data import questions_and_aswers
from pages.home_page import HomePageScooter

class TestFaq:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.step(f'Проверить соответствие ответа вопросу')
    def verify_faq_answer_by_question_index(self, actual_pair, index):
        assert actual_pair == questions_and_aswers.get(index), "Содержание вопроса или ответа не соответствует ожиданиям"

    @allure.step(f'Проверить, что ответ развёрнут')
    def verify_faq_answer_expanded(self, page, index):
        assert not page.section_is_collapsed(index), 'Ответ на вопрос не отображается'

    @allure.title('Проверка соответствия ответов вопросам в секции "Вопросы о важном"')
    @allure.description('В тесте проверяется порядок вопросов, содержание вопросов и ответов и соответствие ответов вопросам.')
    @pytest.mark.parametrize('option_index', [0,1,2,3,4,5,6,7])
    def test_answers_matching_questions_in_faq_section(self, option_index):

        home_page = HomePageScooter(self.driver)
        home_page.open_home_page_by_direct_url()

        actual_pair=home_page.get_question_and_answer_by_option_index(option_index)

        @allure.step(f'Кликнуть по вопросу №{option_index + 1}')
        def click_on_question_by_index(page, index):
            page.click_on_faq_option_by_index(index)

        click_on_question_by_index(home_page,option_index)

        self.verify_faq_answer_by_question_index(actual_pair, option_index)
        self.verify_faq_answer_expanded(home_page, option_index)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
