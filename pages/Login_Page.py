from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Login_page(Base):

    url = 'https://www.campsaver.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    sign_in_button_main_menu = '//a[@id="sign-in-popup-button"]'
    user_name = '//input[@id="signInEmailInput"]'
    password = '//input[@id="signInPasswordInput"]'
    sign_in_button_sign_in_menu = '//button[@class="IRGItx ScEGVe"]'
    sign_as_guest = '//a[@class="PGsc96 iyO3lh BgpWoY"]'
    sign_in_word = '//div[@class="mLqHdi"]'

    # Getters

    def get_sign_in_button_main_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button_main_menu)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_sign_in_button_sign_in_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button_sign_in_menu)))

    def get_sign_in_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_word)))

    def get_as_guest_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_as_guest)))

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('Input email')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input password')

    def click_sign_in_button_sign_in_menu(self):
        self.get_sign_in_button_sign_in_menu().click()
        print('Click sign in button in sign in menu')

    def click_sign_in_button_main_menu(self):
        self.get_sign_in_button_main_menu().click()
        print('Click sign in button in main menu')

    def click_sign_as_guest_button(self):
        self.get_as_guest_button().click()
        print('Click sign in as guest button')

    # Methods
    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.check_url('https://www.campsaver.com/')
        self.click_sign_in_button_main_menu()
        self.get_current_url()
        self.check_url('https://www.campsaver.com/signin')
        self.input_user_name('poyefo1751@dronetz.com')
        self.input_password('Stronghold123')
        self.click_sign_in_button_sign_in_menu()
        self.word_check(self.get_sign_in_word(), 'Please Enter Verification Code')
        self.click_sign_as_guest_button()
        self.get_current_url()
        self.check_url('https://www.campsaver.com/')



