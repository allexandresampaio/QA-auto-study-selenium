from selenium import webdriver


class PageObject:

    def __init__(self, driver=None, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == "Chrome":
                self.driver = webdriver.Chrome()
            elif browser == "Safari":
                self.driver = webdriver.Safari()
            elif browser == "Firefox":
                self.driver = webdriver.Firefox()
            else:
                raise Exception('Browser não suportado!')

    def is_url(self, myURL):
        return self.driver.current_url == myURL

    def close(self):
        self.driver.quit()
