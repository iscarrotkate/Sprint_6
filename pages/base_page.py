from selenium.webdriver.common.by import By
import allure

class BasePageScooter:

    order_button = [By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[contains(text(),'Заказать')]"]
    yandex_logo = [By.XPATH, "//img[@alt='Yandex']"]
    scooter_logo = [By.XPATH, "//img[@alt='Scooter']"]
    confirm_cookie_button = [By.XPATH, "//button[@id='rcc-confirm-button']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликнуть по логотипу "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step('Кликнуть по логотипу "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step('Кликнуть по кнопке "Заказать" в шапке страницы')
    def click_place_order_button(self):
        self.driver.find_element(*self.order_button).click()

    def cookie_popup_is_displayed(self):
        try:
            return self.driver.find_element(*self.confirm_cookie_button).is_displayed()
        except:
            return False

    def confirm_cookies(self):
        self.driver.find_element(*self.confirm_cookie_button).click()
