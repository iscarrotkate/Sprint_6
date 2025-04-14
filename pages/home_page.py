from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers.urls import home_page_url

class HomePageScooter:

    page_url = home_page_url
    header = [By.XPATH, "//div[@class='Home_Header__iJKdX']"]
    order_button = [By.XPATH, "//div[@class='Home_RoadMap__2tal_']//button[contains(text(),'Заказать')]"]
    accordion_questions = [By.XPATH, "(//div[@class='accordion__item'])"]
    accordion_answers = [By.XPATH, "(//div[@class='accordion__panel'])"]
    faq_section = [By.XPATH, "//div[@class='Home_FourPart__1uthg']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть главную страницу')
    def open_home_page_by_direct_url(self):
        self.driver.get(self.page_url)

    @allure.step('Кликнуть по кнопке "Заказать" внизу страницы')
    def click_place_order_button(self):
        order_button = self.driver.find_element(*self.order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='Home_RoadMap__2tal_']//button[contains(text(),'Заказать')]")))
        order_button.click()

    def get_question_and_answer_by_option_index(self, option_index):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.faq_section))

        question = self.driver.find_elements(*self.accordion_questions)[option_index].text
        answer = self.driver.find_elements(*self.accordion_answers)[option_index].get_attribute("innerText")
        return {question: answer}

    def section_is_collapsed(self, option_number):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.faq_section))

        return self.driver.find_elements(*self.accordion_answers)[option_number].get_attribute("hidden")

    def click_on_faq_option_by_index(self, option_index):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.faq_section))

        self.driver.find_elements(*self.accordion_questions)[option_index].click()
