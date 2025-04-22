from random import randint

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import *

class BasePageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить элемент по xpath')
    def get_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    @allure.step('Получить список элементов по xpath')
    def get_list_of_elements_by_xpath(self, xpath):
        return self.driver.find_elements(By.XPATH, xpath)

    @allure.step('Ждать, пока элемент не станет кликабельным')
    def wait_for_element_to_be_clickable(self, element):
        try:
            return WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            element))
        except:
            return 'Не удалось определить кликабельность элемента'

    @allure.step('Открыть страницу по прямому URL')
    def open_page_by_direct_url(self, url):
        self.driver.get(url)

    @allure.step('Получить URL текущей страницы')
    def get_current_page_url(self):
        return self.driver.current_url

    @allure.step('Проскролить страницу до элемента')
    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            return 'Не удалось осуществить скролл до указанного элемента'

    @allure.step('Проверить соответствие текущего URL ожидаемому')
    def verify_current_url_is_expected(self, expected_url):
        assert self.driver.current_url == expected_url

    @allure.step('Заполнить поле для ввода значением')
    def fill_input_element_with_value(self, xpath, value):
        self.driver.find_element(By.XPATH, xpath).send_keys(value)

    @allure.step('Проверить отображается ли элемент')
    def element_is_displayed_by_xpath(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath).is_displayed()
        except:
            return False

    @allure.step('Закрыть куки попап, если отображается')
    def close_cookie_popup(self):
        if self.element_is_displayed_by_xpath(base_page_confirm_cookie_button):
            self.get_element_by_xpath(base_page_confirm_cookie_button).click()

    @allure.step('Кликнуть по элементу')
    def click_on_element_by_xpath(self, xpath):
        self.get_element_by_xpath(xpath).click()

    @allure.step('Кликнуть по случайному элементу из списка')
    def click_on_random_item_from_list(self, elements_xpath):
        elements_list = self.driver.find_elements(By.XPATH, elements_xpath)
        elements_list[randint(0, len(elements_list) - 1)].click()

    @allure.step('Ждать, пока элемент не отобразится')
    def wait_for_element_to_be_visible(self, element):
        try:
            return         WebDriverWait(self.driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, element)))
        except:
            return 'Не удалось определить видимость элемента'

    @allure.step('Ждать указанный таймаут')
    def wait_for_timeout(self, timeout):
        WebDriverWait(self.driver, timeout)

    @allure.step('Переключиться на вкладку браузера')
    def switch_browser_tab(self, tab_index):
        self.driver.switch_to.window(self.driver.window_handles[tab_index])

    @allure.step('Кликнуть по логотипу "Яндекс"')
    def click_yandex_logo(self):
        el = self.driver.find_element(By.XPATH, base_page_yandex_logo)
        el.click()

    @allure.step('Кликнуть по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(By.XPATH, base_page_scooter_logo).click()
