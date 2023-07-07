import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support.select import Select


class Client_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    email = '//input[@id="op_order_checkout_email"]'
    country_select = "//select[@id='shipping-country']/option[@selected='selected']"
    first_name = '//input[@id="op_order_checkout_shippingAddress_firstName"]'
    last_name = '//input[@id="op_order_checkout_shippingAddress_lastName"]'
    street_address = '//input[@id="op_order_checkout_shippingAddress_addressOne"]'
    citi = '//input[@id="op_order_checkout_shippingAddress_city"]'
    zip_code = '//input[@id="op_order_checkout_shippingAddress_zip"]'
    phone = '//input[@id="op_order_checkout_shippingAddress_phone"]'
    # card_number = '//input[@id="credit-card-number"]'
    # exp_month = '//select[@id="expiration-month"]'
    # exp_year = '//select[@id="expiration-year"]'
    # cvv = '//input[@id="cvv"]'
    continue_button = '//input[@class="submit-order-button checkout-submit qa-shipping-method-selected"]'
    error_message = '//span[@class="input-error-message e-form__error e-form__error_no-margin"]'

    # Getters
    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_country_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.country_select)))

    def get_country_select_select(self):
        return Select(self.get_country_select())

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.citi)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street_address)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    # def get_card_number(self):
    #     return self.driver.find_element(By.XPATH, self.card_number)
    #
    # def get_exp_month(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exp_month)))
    #
    # def get_exp_month_select(self):
    #     return Select(self.get_exp_month())
    #
    # def get_exp_year(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exp_year)))
    #
    # def get_exp_year_select(self):
    #     return Select(self.get_exp_year())
    #
    # def get_cvv(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cvv)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_error_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.error_message)))

    # Actions
    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input user email')

    def check_country(self, country):
        print(f'Checking country {country}')
        self.word_check(self.get_country_select(), country)

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input user first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input user last name')

    def input_street(self, street):
        self.get_street().send_keys(street)
        print('Input user street')

    def input_city(self, city):
        self.get_city().send_keys(city)
        print('Input user city')

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print('Input user zip code')

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print('Input user phone')

    # def input_card_number(self, number):
    #     self.get_card_number().click()
    #     print('Input user card number')
    #
    # def input_card_month(self, month):
    #     self.get_exp_month_select().select_by_index(month)
    #     print('Input user card exp month')
    #
    # def input_card_year(self, year):
    #     self.get_exp_year_select().select_by_index(year)
    #     print('Input user card exp year')
    #
    # def input_card_cvv(self, cvv):
    #     self.get_cvv().send_keys(cvv)
    #     print('Input user card cvv')

    def continue_to_checkout(self):
        self.get_continue_button().click()
        print('Going to check out')

    def check_error(self, error):
        print('Checking card payment error')
        self.word_check(self.get_error_message(), error)

    # Methods
    def confirm_credentials(self):
        self.get_current_url()
        self.check_url('https://www.campsaver.com/checkout/step2')
        self.input_email('poyefo1751@dronetz.com')
        self.check_country('Albania')
        self.input_first_name('Aleks')
        self.input_last_name('Ivanov')
        self.input_street('Rruga Dervish Hekali 79')
        self.input_city('Tiranë')
        self.input_zip_code('1001')
        self.input_phone('042226334')
        time.sleep(2)
        # self.input_card_number('5374921147186089')
        # self.input_card_month(6)
        # self.input_card_year(4)
        # self.input_card_cvv('666')
        self.continue_to_checkout()
        self.check_error('Please review your credit card information.')
