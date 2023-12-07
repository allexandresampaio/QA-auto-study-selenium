from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class CheckoutOnePage(PageObject):
    myURL = 'https://www.saucedemo.com/checkout-step-one.html'
    txt_id_continue_button = 'continue'
    id_first_name_field = 'first-name'
    id_last_name_field = 'last-name'
    id_postal_code_field = 'postal-code'

    def __init__(self, driver):
        super(CheckoutOnePage, self).__init__(driver=driver)

    def is_url_checkout_one(self):
        return self.is_url(self.myURL)

    def go_to_checkout_two(self):
        first_name = self.driver.find_element(By.ID, value=self.id_first_name_field)
        first_name.send_keys('First')
        last_name = self.driver.find_element(By.ID, value=self.id_last_name_field)
        last_name.send_keys('Last')
        postal_code = self.driver.find_element(By.ID, value=self.id_postal_code_field)
        postal_code.send_keys('AAA-0000')

        checkout_button = self.driver.find_element(By.ID, value=self.txt_id_continue_button)
        checkout_button.click()
        return self.driver
