from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.PageObject import PageObject


class MenuPage(PageObject):
    id_menu_button = 'react-burger-menu-btn'
    id_menu_cross_button = 'react-burger-cross-btn'
    id_menu_logout_button = 'logout_sidebar_link'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def has_menu(self):
        try:
            menu_element = self.driver.find_element(By.ID, value=self.id_menu_button)
        except NoSuchElementException:
            return False
        return menu_element.is_displayed()

    def open_menu(self):
        self.driver.find_element(By.ID, self.id_menu_button).click()

    def is_menu_open(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.ID, self.id_menu_cross_button)
            )
        )
        return self.driver.find_element(By.ID, self.id_menu_cross_button).is_displayed()

    def click_logout(self):
        return self.driver.find_element(By.ID, self.id_menu_logout_button).click()
