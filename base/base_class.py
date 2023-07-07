import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url is: ' + get_url)

    """Login check method"""
    def word_check(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f'Word "{result}" checked!')

    """Method Screenshoot"""
    def get_screenshoot(self):
        now_time = datetime.datetime.utcnow().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshoot = 'screenshot' + now_time + '.png'
        self.driver.save_screenshot('C:\\Users\\Alx\\PycharmProjects\\7.15project\\screen\\' + name_screenshoot + '.png')

    """Method check url"""
    def check_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('URLs mathces!')

    """Method Grand Total Check"""
    def grand_total_check(self, order, shipping, grand):
        assert float(order.replace('$', '')) + float(shipping.replace('$', '')) == float(grand.replace('$', ''))
        print('Grand total calculated right!')

    """Product price check"""
    def product_price_checking(self, firs_price, cart_price):
        assert firs_price == cart_price
        print('1st item price and cart price matches!')
