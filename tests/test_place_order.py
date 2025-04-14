import allure
import pytest

from helpers.data import user_min_length, user_max_length
from pages.place_order_page import PlaceOrderPageScooter

from selenium import webdriver

class TestPlaceOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка оформления заказа')
    @allure.description('В тесте проверяется оформление заказа пользователем с валидными водными персональными данными и данными о заказе')
    @pytest.mark.parametrize('user', [user_min_length, user_max_length])
    def test_place_order_via_order_button_at_home_page(self, user):

        place_order_page = PlaceOrderPageScooter(self.driver)

        place_order_page.open_place_order_page_by_direct_url()

        place_order_page.fill_in_personal_data(user)
        place_order_page.click_next_button()
        place_order_page.fill_in_order_data()
        place_order_page.click_place_order_button()
        place_order_page.click_confirm_order_placement()
        place_order_page.verify_order_confirmation_popup_is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
