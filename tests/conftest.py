import pytest

from pages.LoginPage import LoginPage


# as it is named as setup, pytest knows it's a setup method and has to be executed.
# if named with something else, has to use @pytest.fixture one line before
# and also use it as a precondition for each test, see alternative lines

@pytest.fixture
def open_browser():
    login_page = LoginPage(browser='Chrome')

    yield login_page
    # quit browser
    login_page.close()


@pytest.fixture
def login_saucedemo(open_browser):
    login_page = open_browser
    login_page.enter_login()
    yield login_page
