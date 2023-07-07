# import time
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    products_group_1 = '//a[@href="https://www.campsaver.com/camp-hike.html"]'
    products_category_1 = '(//span[@class="grid__text"])[1]'
    in_stock_only_switch = '//div[@data-id="in-stock"]'
    volume_filter = '//div[@data-id="range-50-70-liters"]'
    price_from = '//input[@class="e-sidebar-custom-price__field-min e-custom-price__field-input op-plugin op-widget-initialized"]'
    price_to = '//input[@class="e-sidebar-custom-price__field-max e-custom-price__field-input op-plugin op-widget-initialized"]'
    price_range_go_button = '//button[@class="e-custom-price__apply e-custom-price__apply_btn e-menu__li_back_prices"]'
    product_1 = '(//span[@class="variant-price-dollars"])[8]'
    add_to_cart = '//button[@class="IRGItx mckE1s c3VNsn E1q2f9"]'
    banner_close = '//button[@aria-label="Close"]'
    cart = '//span[@class="e-header-shopping-cart__text"]'
    camp_hike_check = '//div[@id="page-header-text"]'
    selected_item_price = '//span[@class="PvloAJ"]'
    selected_item_price_in_cart = '//span[@class="e-order-summary-heading__new"]'

    # Getters

    def get_product_group_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.products_group_1)))

    def get_product_category_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.products_category_1)))

    def get_in_stock_only_switch(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.in_stock_only_switch)))

    def get_volume_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.volume_filter)))

    def get_price_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_from)))

    def get_price_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_to)))

    def get_price_range_go_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_range_go_button)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_banner_close(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.banner_close)))

    def get_camp_hike_check(self):
        return self.driver.find_element(By.XPATH, self.camp_hike_check)

    def get_selected_item_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_item_price)))

    def get_selected_item_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.selected_item_price_in_cart)))

    # Actions
    def go_product_group_1(self):
        self.get_product_group_1().click()
        self.get_product_group_1().click()
        print('Go to product group 1')

    def go_product_category_1(self):
        self.get_product_category_1().click()
        print('Go to product category 1')

    def use_in_stock_only_switch(self):
        self.get_in_stock_only_switch().click()
        print('Use "in stock only"')

    def use_volume_filter(self):
        self.get_volume_filter().click()
        print('Choose volume of product')

    def set_price_from(self, price_from):
        self.get_price_from().send_keys(price_from)
        print(f'Set "From price" to {price_from}')

    def set_price_to(self, price_to):
        self.get_price_to().send_keys(price_to)
        print(f'Set "To price" to {price_to}')

    def press_price_range_go_button(self):
        self.get_price_range_go_button().click()
        print("Apply price filter")

    def add_product_1(self):
        time.sleep(3)
        self.get_product_1().click()
        print("Click product 1")

    def press_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Add to cart product 1')

    def going_to_cart(self):
        time.sleep(3)
        self.get_banner_close().click()
        self.get_cart().click()
        print('Going to cart')

    # Methods
    def select_product_1(self):
        self.go_product_group_1()
        self.get_current_url()
        time.sleep(1)
        self.check_url('https://www.campsaver.com/camp-hike.html')
        self.go_product_category_1()
        self.get_current_url()
        time.sleep(1)
        self.check_url('https://www.campsaver.com/backpacks.html')
        self.use_in_stock_only_switch()
        self.set_price_from('100')
        self.set_price_to('145')
        self.press_price_range_go_button()
        self.use_volume_filter()
        self.add_product_1()
        self.press_add_to_cart_button()
        sel_it_price = self.get_selected_item_price().text
        self.going_to_cart()
        self.product_price_checking(sel_it_price, self.get_selected_item_price_in_cart().text)
