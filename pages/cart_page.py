# import time
import time
from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support.select import Select

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    selected_item_price = '//td[@class="variant-a cart-basket-price"]'
    order_subtotal = '//td[@id="shipping_total_subtotal"]'
    country_select = '//select[@id="shipping-country"]'
    shipping_price = '//div[@class="e-shipping-methods__preview-amount"]'
    grand_total = '//span[@class="order-summary-price cart-checkout-right-panel-header shipping_total_grandtotal"]'
    checkout_button = '//input[@class="checkout-button cart-event-tracking checkout-submit"]'
    order_summary_checkout = '//span[@class="order-summary-price cart-checkout-right-panel-header shipping_total_grandtotal"]'

    # Getters
    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_selected_item_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_item_price)))

    def get_order_subtotal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_subtotal)))

    def get_country_select(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.country_select)))

    def get_country_select_select(self):
        return Select(self.get_country_select())

    def get_shipping_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_price)))

    def get_grand_total(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.grand_total)))

    def get_order_summary_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_summary_checkout)))

    # Actions
    def country_selecting_menu(self):
        time.sleep(2)
        self.get_country_select_select().select_by_index(4)

    def go_to_checkout_page(self):
        self.get_checkout_button().click()

    # Methods
    def check_out(self):
        self.get_current_url()
        time.sleep(1)
        self.check_url('https://www.campsaver.com/checkout/cart')
        print('Selecting "Albania"')
        self.country_selecting_menu()
        print(f'Product 1 price: {self.get_order_subtotal().text}')
        print(f'Delivery price of Product 1: {self.get_shipping_price().text}')
        print(f'Grand total is: {self.get_grand_total().text}')
        total = self.get_grand_total().text
        self.grand_total_check(self.get_order_subtotal().text, self.get_shipping_price().text, self.get_grand_total().text)
        self.get_screenshoot()
        self.go_to_checkout_page()
        print('Checking checkout grand total:')
        self.grand_total_check(total, '0', self.get_order_summary_checkout().text)
