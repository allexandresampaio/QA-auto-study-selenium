from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutFinishPage(PageObject):
    myURL = 'https://www.saucedemo.com/checkout-complete.html'
    txt_class_finish_header = 'complete-header'
    txt_header_finish = 'Thank you for your order!'

    def __init__(self, driver):
        super(CheckoutFinishPage, self).__init__(driver=driver)

    def is_url_checkout_completed(self):
        return self.is_url(self.myURL)

    def is_checkout_completed(self):
        finish_header = self.driver.find_element(By.CLASS_NAME, value=self.txt_class_finish_header).text
        return finish_header == self.txt_header_finish
