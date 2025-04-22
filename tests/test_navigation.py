import allure
from selenium import webdriver

from helpers.urls import dzen_url, home_page_url, base_url
from locators.external_locators import dzen_home_page_logo

from pages.home_page import HomePageScooter
from pages.place_order_page import PlaceOrderPageScooter


class TestNavigation:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка открытия страницы оформления заказа по кнопке в конце страницы')
    @allure.description('В тесте проверяется, что при клике по кнопке "Заказать" в конце страницы открывается страница оформления заказа')
    def test_navigate_to_place_order_page_via_body(self):
        home_page = HomePageScooter(self.driver)

        home_page.open_home_page_by_direct_url()
        home_page.click_place_order_button_bottom()
        home_page.verify_place_order_page_is_opened()

    @allure.title('Проверка открытия страницы оформления заказа по кнопке в шапке страницы')
    @allure.description('В тесте проверяется, что при клике по кнопке "Заказать" в шапке страницы открывается страница оформления заказа')
    def test_navigate_to_place_order_page_via_header(self):
        home_page = HomePageScooter(self.driver)

        home_page.open_home_page_by_direct_url()
        home_page.click_place_order_button_top()
        home_page.verify_place_order_page_is_opened()

    @allure.title('Проверка открытия главной страницы Яндекс.Дзен при клике на логотип "Яндекс" в шапке страницы')
    @allure.description('В тесте проверяется, что при клике на логотип "Яндекс" открывается страница Яндекс.Дзен')
    def test_navigate_to_dzen_via_logo(self):
        place_order_page = PlaceOrderPageScooter(self.driver)
        place_order_page.open_place_order_page_by_direct_url()
        place_order_page.click_yandex_logo()

        place_order_page.wait_for_timeout(10)
        place_order_page.switch_browser_tab(1)
        place_order_page.wait_for_element_to_be_visible(dzen_home_page_logo)

        place_order_page.verify_current_url_is_expected(dzen_url)

    @allure.title('Проверка открытия главной страницы самоката при клике на логотип "Самокат"')
    @allure.description('В тесте проверяется, что при клике с на логотип "Самокат" в шапке страницы открывается главная страница самоката')
    def test_navigate_to_home_via_logo(self):
        place_order_page = PlaceOrderPageScooter(self.driver)
        place_order_page.open_place_order_page_by_direct_url()
        place_order_page.click_scooter_logo()

        place_order_page.verify_current_url_is_expected(f'{base_url}{home_page_url}')


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
