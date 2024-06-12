from selenium.webdriver.common.by import By
from pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage(PageObject):
    myURL = 'https://bbc.com/'
    class_login_error_msg = 'error-message-container'
    top_bar_class_name = 'sc-49542412-0 bbWPuq'
    top_bar_menu_button_class_name = 'sc-49542412-3 ipGSFC'
    top_bar_find_button_class_name = 'sc-49542412-3 sc-49542412-4 ipGSFC eojOvQ'
    top_bar_logo_class_name = 'sc-2e6baa30-0 gILusN'
    top_bar_logo_txt = 'British Broadcasting Corporation'
    top_bar_button_register_class_name = 'sc-84b18709-2 sc-84b18709-3 ifKcIh hMxlKQ'
    top_bar_button_register_txt = 'Register'
    top_bar_button_signin_class_name = 'sc-84b18709-2 sc-84b18709-5 ifKcIh hYXWsv'
    top_bar_button_signin_txt = 'Sign In'

    def __init__(self, browser):
        super(HomePage, self).__init__(browser=browser)
        self.open()

    def open(self):
        self.driver.get(self.myURL)

    def is_url_homepage(self):
        return self.is_url(self.myURL)

    def has_top_bar(self):
        return self.driver.find_element(By.CLASS_NAME, value=self.class_title).text == self.txt_title_products


    def check_basic_info(self):

        pass
