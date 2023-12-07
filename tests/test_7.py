import pytest
from selenium.common import NoSuchElementException

from pages.ProductsPage import ProductsPage


class Test7:

    def test_sort(self, open_browser):
        login_page = open_browser
        login_page.enter_login()
        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_url_product(), 'Página incorreta!'
        assert products_page.has_title_products(), 'Página incorreta!'

        products_page.select_sort_low_to_high()
        try:
            inventory_list = products_page.find_all_elements()
        except NoSuchElementException:
            pytest.fail('Lista de produtos indisponível.')
        assert products_page.sorting_is_correct(inventory_list), 'Ordem dos produtos não está de acordo.'
