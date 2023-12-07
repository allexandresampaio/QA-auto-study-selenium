from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class YourCartPage(PageObject):
    cart_URL = 'https://www.saucedemo.com/cart.html'
    txt_class_inventory_item = 'inventory_item_name'
    txt_class_checkout_button = 'checkout_button'

    def __init__(self, driver):
        super(YourCartPage, self).__init__(driver=driver)

    def is_url_cart(self):
        return self.is_url(self.cart_URL)

    def cart_has_product_for_checkout(self, product_selected_title):
        return self.driver.find_element(By.CLASS_NAME,
                                        value=self.txt_class_inventory_item).text == product_selected_title

    def go_to_checkout(self):
        checkout_button = self.driver.find_element(By.CLASS_NAME, value=self.txt_class_checkout_button)
        checkout_button.click()
        return self.driver
