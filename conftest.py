import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

g = Service('C:\\Users\\Alx\\PycharmProjects\\OOP\\geckodriver.exe')
options = webdriver.FirefoxOptions()
options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
driver = webdriver.Firefox(options=options, service=g)

@pytest.fixture()
def set_up():
    print('\nStart test ' + '*' * 150)

    yield
    print('\nFinish test ' + '*' * 150)
    print('Exit system')
    driver.quit()
