import allure

from helpers.data import questions_and_aswers
from locators.base_page_locators import base_page_order_button
from pages.base_page import BasePageScooter
from helpers.urls import place_order_page_url, base_url
from locators.home_page_locators import *


class HomePageScooter(BasePageScooter):
    page_url = f'{base_url}{place_order_page_url}'

    @allure.step('Открыть главную страницу')
    def open_home_page_by_direct_url(self):
        self.open_page_by_direct_url(base_url)

    @allure.step('Кликнуть по кнопке "Заказать" в конце страницы')
    def click_place_order_button_bottom(self):
        order_button = self.get_element_by_xpath(home_page_order_button)

        self.scroll_to_element(order_button)
        self.wait_for_element_to_be_clickable(order_button)
        order_button.click()

    @allure.step('Кликнуть по кнопке "Заказать" в шапке страницы')
    def click_place_order_button_top(self):
        order_button = self.get_element_by_xpath(base_page_order_button)

        self.scroll_to_element(order_button)
        self.wait_for_element_to_be_clickable(order_button)
        order_button.click()

    @allure.step('Проверить, что открыта страница оформления заказа')
    def verify_place_order_page_is_opened(self):
        self.verify_current_url_is_expected(f'{base_url}{place_order_page_url}')

    @allure.step('Получить фактический список пар "вопрос: ответ"')
    def get_question_and_answer_by_option_index(self, option_index):
        faq_section = self.get_element_by_xpath(home_page_faq_section)
        self.scroll_to_element(faq_section)

        question = self.get_list_of_elements_by_xpath(home_page_accordion_questions)[option_index].text
        answer = self.get_list_of_elements_by_xpath(home_page_accordion_answers)[option_index].get_attribute(
            "innerText")
        return {question: answer}

    @allure.step('Кликнуть по секции с вопросом')
    def click_on_question_by_index(self, index):
        faq_section = self.get_element_by_xpath(home_page_faq_section)
        self.scroll_to_element(faq_section)

        element = self.get_list_of_elements_by_xpath(home_page_accordion_questions)[index]
        self.wait_for_element_to_be_clickable(element)
        element.click()

    @allure.step('Проверить, что секция с ответом развёрнута')
    def verify_faq_answer_expanded(self, option_index):
        faq_section = self.get_element_by_xpath(home_page_faq_section)
        self.scroll_to_element(faq_section)

        assert not self.get_list_of_elements_by_xpath(home_page_accordion_answers)[option_index].get_attribute("hidden")

    @allure.step('Проверить, что ответ соответствует вопросу')
    def verify_faq_answer_by_question_index(self, index):
        assert self.get_question_and_answer_by_option_index(index) == questions_and_aswers.get(index)
