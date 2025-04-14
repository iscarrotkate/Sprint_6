from random import randint

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers.urls import place_order_page_url
from locators.place_order_page_locators import *

from selenium.webdriver.common.by import By

from pages.base_page import BasePageScooter


class PlaceOrderPageScooter:

    page_url = place_order_page_url

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу оформления заказа')
    def open_place_order_page_by_direct_url(self):
        self.driver.get(self.page_url)

    @allure.step('Заполнить персональные данные')
    def fill_in_personal_data(self, user):
        self.driver.find_element(By.XPATH, place_order_first_name_input).send_keys(user['Имя'])
        self.driver.find_element(By.XPATH, place_order_last_name_input).send_keys(user['Фамилия'])
        self.driver.find_element(By.XPATH, place_order_address_input).send_keys(user['Адрес'])
        self.select_station_by_name(user['Метро'])
        self.driver.find_element(By.XPATH, place_order_phone_number_input).send_keys(user['Телефон'])

    @allure.step('Заполнить данные о заказе')
    def fill_in_order_data(self):
        self.select_tomorrow_in_date_in_date_picker()
        self.driver.find_element(By.XPATH, place_order_term_date_dropdown).click()
        terms_list = self.driver.find_elements(By.XPATH, place_order_terms_list)
        terms_list[randint(0, len(terms_list) - 1)].click()
        colors_list = self.driver.find_elements(By.XPATH, place_order_color_checkboxes)
        colors_list[randint(0, len(colors_list) - 1)].click()
        self.driver.find_element(By.XPATH, place_order_comment_input).send_keys('Хорошего дня!')

    @allure.step('Кликнуть по кнопке "Далее"')
    def click_next_button(self):
        self.driver.find_element(By.XPATH, place_order_next_button).click()

    @allure.step('Кликнуть по кнопке "Заказать"')
    def click_place_order_button(self):
        self.driver.find_element(By.XPATH, place_order_order_button).click()

    @allure.step('Кликнуть по кнопке подтверждения заказа')
    def click_confirm_order_placement(self):
        WebDriverWait(self.driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, place_order_confirmation_popup)))
        self.driver.find_element(By.XPATH, place_order_confirmation_popup_yes).click()

    def select_tomorrow_in_date_in_date_picker(self):
        self.driver.find_element(By.XPATH, place_order_delivery_date_input).click()
        dates_list = self.driver.find_elements(By.XPATH, place_order_date_picker_dates)
        current_day = False
        for day in dates_list:
            if current_day == False:
                if 'today' in day.get_attribute("class"):
                    current_day = True
            else:
                day.click()
                break

    def order_placed_confirmation_is_displayed(self):
        WebDriverWait(self.driver, 3)
        return self.driver.find_element(By.XPATH, place_order_order_placed_confirmation_popup).is_displayed()

    def select_station_by_name(self, name):
        base_page = BasePageScooter(self.driver)
        if base_page.cookie_popup_is_displayed() == True:
            base_page.confirm_cookies()

        self.driver.find_element(By.XPATH, place_order_subway_dropdown).click()
        stations = self.driver.find_elements(By.XPATH, place_order_stations_list)

        for station in stations:
            if station.text == name:
                station.click()
                break
