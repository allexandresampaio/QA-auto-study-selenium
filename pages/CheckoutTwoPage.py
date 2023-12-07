from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutTwoPage(PageObject):
    myURL = 'https://www.saucedemo.com/checkout-step-two.html'
    txt_id_finish_button = 'finish'
    txt_class_product_title = 'inventory_item_name'

    def __init__(self, driver):
        super(CheckoutTwoPage, self).__init__(driver=driver)

    def is_url_checkout_two(self):
        return self.is_url(self.myURL)

    def go_to_finish(self):
        finish_button = self.driver.find_element(By.ID, value=self.txt_id_finish_button)
        finish_button.click()
        return self.driver

    def product_summary_is_correct(self, product_selected_title):
        product_title = self.driver.find_element(By.CLASS_NAME, value=self.txt_class_product_title).text
        return product_title == product_selected_title
