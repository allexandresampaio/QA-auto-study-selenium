from selenium.webdriver.common.by import By

from pages.PageObject import PageObject


class LoginPage(PageObject):
    myURL = 'https://www.saucedemo.com/'
    id_login_button = 'login-button'
    class_login_error_msg = 'error-message-container'
    txt_username_is_required = 'Epic sadface: Username is required'
    id_username_field = 'user-name'
    id_password_field = 'password'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.open()

    def open(self):
        self.driver.get(self.myURL)

    def click_login_button(self):
        self.driver.find_element(By.ID, value=self.id_login_button).click()

    def is_url_login(self):
        return self.is_url(self.myURL)

    def has_login_error_message(self):
        error_message = self.driver.find_element(By.CLASS_NAME, value=self.class_login_error_msg).text
        return error_message == self.txt_username_is_required

    def enter_login(self, username='user-name', password='password'):
        username = self.driver.find_element(By.ID, value=self.id_username_field)
        username.send_keys('standard_user')
        password = self.driver.find_element(By.ID, value=self.id_password_field)
        password.send_keys('secret_sauce')
        self.click_login_button()
