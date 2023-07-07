import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from pages.Login_Page import Login_page
from pages.cart_page import Cart_page
from pages.Client_Page import Client_page
from pages.Main_Page import Main_page


def test_buy_product(set_up):
    g = Service('C:\\Users\\Alx\\PycharmProjects\\OOP\\geckodriver.exe')
    options = webdriver.FirefoxOptions()
    options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(options=options, service=g)

    login = Login_page(driver)
    login.autorization()

    main_page = Main_page(driver)
    main_page.select_product_1()

    checkout = Cart_page(driver)
    checkout.check_out()

    credentials = Client_page(driver)
    credentials.confirm_credentials()



