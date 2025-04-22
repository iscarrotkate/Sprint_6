import allure

from locators.place_order_page_locators import *
from pages.base_page import BasePageScooter
from helpers.urls import base_url, place_order_page_url


class PlaceOrderPageScooter(BasePageScooter):
    page_url = f'{base_url}{place_order_page_url}'

    @allure.step('Открыть страницу оформления заказа')
    def open_place_order_page_by_direct_url(self):
        self.open_page_by_direct_url(self.page_url)

    @allure.step('Заполнить персональные данные')
    def fill_in_personal_data(self, user):
        self.fill_input_element_with_value(place_order_first_name_input, user['Имя'])
        self.fill_input_element_with_value(place_order_last_name_input, user['Фамилия'])
        self.fill_input_element_with_value(place_order_address_input, user['Адрес'])
        self.select_station_by_name(user['Метро'])
        self.fill_input_element_with_value(place_order_phone_number_input, user['Телефон'])

    @allure.step('Кликнуть по кнопке "Далее"')
    def click_next_button(self):
        self.click_on_element_by_xpath(place_order_next_button)

    @allure.step('Заполнить данные о заказе')
    def fill_in_order_data(self):
        self.select_tomorrow_in_date_in_date_picker()
        self.click_on_element_by_xpath(place_order_term_date_dropdown)
        self.click_on_random_item_from_list(place_order_terms_list)
        self.click_on_random_item_from_list(place_order_color_checkboxes)
        self.fill_input_element_with_value(place_order_comment_input, 'Хорошего дня!')

    @allure.step('Кликнуть по кнопке "Заказать"')
    def click_place_order_button(self):
        self.click_on_element_by_xpath(place_order_order_button)

    @allure.step('Кликнуть по кнопке подтверждения заказа')
    def click_confirm_order_placement(self):
        self.wait_for_element_to_be_visible(place_order_confirmation_popup)
        self.click_on_element_by_xpath(place_order_confirmation_popup_yes)

    @allure.step('Проверить, что отображается модальное окно с подтверждением заказа')
    def verify_order_confirmation_popup_is_displayed(self):
        self.wait_for_timeout(3)
        assert self.get_element_by_xpath(place_order_order_placed_confirmation_popup).is_displayed()

    @allure.step('Выбрать день доставки')
    def select_tomorrow_in_date_in_date_picker(self):
        self.click_on_element_by_xpath(place_order_delivery_date_input)
        dates_list = self.get_list_of_elements_by_xpath(place_order_date_picker_dates)
        current_day = False
        for day in dates_list:
            if not current_day:
                if 'today' in day.get_attribute("class"):
                    current_day = True
            else:
                day.click()
                break

    @allure.step('Выбрать станцию метро')
    def select_station_by_name(self, name):
        self.close_cookie_popup()

        self.click_on_element_by_xpath(place_order_subway_dropdown)
        stations = self.get_list_of_elements_by_xpath(place_order_stations_list)

        for station in stations:
            if station.text == name:
                station.click()
                break

