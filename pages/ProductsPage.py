import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.PageObject import PageObject


class ProductsPage(PageObject):
    myURL = 'https://www.saucedemo.com/inventory.html'
    class_title = 'title'
    txt_title_products = 'Products'
    txt_class_products = 'inventory_item'
    txt_class_inventory_item = 'inventory_item_name'
    txt_button_inventory = 'btn_inventory'
    txt_button_selected_item = 'Remove'
    txt_class_icon_cart = 'shopping_cart_badge'
    txt_class_sort_button = 'product_sort_container'
    txt_container_selected = 'lohi'
    txt_class_inventory_item_price = 'inventory_item_price'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)
        self.item_title = None

    def is_url_product(self):
        return self.is_url(self.myURL)

    def has_title_products(self):
        return self.driver.find_element(By.CLASS_NAME, value=self.class_title).text == self.txt_title_products

    def find_all_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, value=self.txt_class_products)

    def select_random_product_to_cart(self, inventory_list):
        # choosing a random item in the list (that always will bring 6 items)
        random_item = inventory_list[random.randint(0, len(inventory_list) - 1)]
        selected_item_button = random_item.find_element(By.CLASS_NAME, value=self.txt_button_inventory)
        selected_item_button.click()
        self.item_title = random_item.find_element(By.CLASS_NAME, value=self.txt_class_inventory_item).text
        return random_item

    def product_is_in_cart(self, product_selected):
        return product_selected.find_element(By.CLASS_NAME,
                                             value=self.txt_button_inventory).text == self.txt_button_selected_item

    def cart_icon_is_1(self):
        # checking cart icon number
        cart_icon = self.driver.find_element(By.CLASS_NAME, value=self.txt_class_icon_cart)
        return cart_icon.text == '1'

    def go_to_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, value=self.txt_class_icon_cart)
        cart_icon.click()
        return self.driver

    def get_product_title(self):
        return self.item_title

    def select_sort_low_to_high(self):
        select = Select(self.driver.find_element(By.CLASS_NAME, value=self.txt_class_sort_button))
        select.select_by_value(self.txt_container_selected)

    def sorting_is_correct(self, inventory_list):
        values_list = []
        for i in inventory_list:
            price = i.find_element(By.CLASS_NAME, value=self.txt_class_inventory_item_price).text.replace("$", "")
            values_list.append(float(price))

        sorted_values_list = values_list
        sorted_values_list.sort()
        return values_list == sorted_values_list
