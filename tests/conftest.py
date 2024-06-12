import pytest

from pages.HomePage import HomePage


# as it is named as setup, pytest knows it's a setup method and has to be executed.
# if named with something else, has to use @pytest.fixture one line before
# and also use it as a precondition for each test, see alternative lines

@pytest.fixture
def open_browser():
    home_page = HomePage(browser='Chrome')

    yield home_page
    # quit browser
    home_page.close()


@pytest.fixture
def check_basic_info(open_browser):
    home_page = open_browser
    home_page.check_basic_info()
    yield home_page
