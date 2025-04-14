import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers.urls import dzen_url
from locators.external_locators import dzen_home_page_logo
from pages.base_page import BasePageScooter
from pages.home_page import HomePageScooter
from pages.place_order_page import PlaceOrderPageScooter


class TestNavigation:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @staticmethod
    @allure.step(f'Проверить текущий URL')
    def verify_current_url(current_url, expected_url):
        assert current_url == expected_url

    @allure.title('Проверка открытия страницы оформления заказа по кнопке в шапке страницы')
    @allure.description('В тесте проверяется, что при клике по кнопке "Заказать" в шапке страницы открывается страница оформления заказа')
    def test_navigate_to_place_order_page_via_header(self):
        HomePageScooter(self.driver).open_home_page_by_direct_url()
        BasePageScooter(self.driver).click_place_order_button()

        self.verify_current_url(self.driver.current_url, PlaceOrderPageScooter(self.driver).page_url)

    @allure.title('Проверка открытия страницы оформления заказа по кнопке в теле страницы')
    @allure.description('В тесте проверяется, что при клике по кнопке "Заказать" внизу страницы открывается страница оформления заказа')
    def test_navigate_to_place_order_page_via_body(self):
        home_page = HomePageScooter(self.driver)

        home_page.open_home_page_by_direct_url()
        home_page.click_place_order_button()

        self.verify_current_url(self.driver.current_url, PlaceOrderPageScooter(self.driver).page_url)

    @allure.title('Проверка открытия главной страницы Яндекс.Дзен при клике на логотип "Яндекс" в шапке страницы')
    @allure.description('В тесте проверяется, что при клике на логотип "Яндекс" открывается страница Яндекс.Дзен')
    def test_navigate_to_dzen_via_logo(self):
        PlaceOrderPageScooter(self.driver).open_place_order_page_by_direct_url()
        BasePageScooter(self.driver).click_yandex_logo()

        WebDriverWait(self.driver, 10)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, dzen_home_page_logo)))

        self.verify_current_url(self.driver.current_url, dzen_url)

    @allure.title('Проверка открытия главной страницы самоката при клике на логотип "Самокат"')
    @allure.description('В тесте проверяется, что при клике с на логотип "Самокат" в шапке страницы открывается главная страница самоката')
    def test_navigate_to_home_via_logo(self):
        PlaceOrderPageScooter(self.driver).open_place_order_page_by_direct_url()

        BasePageScooter(self.driver).click_scooter_logo()

        self.verify_current_url(self.driver.current_url, HomePageScooter.page_url)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
