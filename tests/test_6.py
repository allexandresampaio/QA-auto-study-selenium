import pytest
from selenium.common import NoSuchElementException

from pages.CheckoutFinishPage import CheckoutFinishPage
from pages.CheckoutOnePage import CheckoutOnePage
from pages.CheckoutTwoPage import CheckoutTwoPage
from pages.ProductsPage import ProductsPage
from pages.YourCartPage import YourCartPage


class Test6:

    def test_checkout(self, open_browser):
        login_page = open_browser
        login_page.enter_login()
        products_page = ProductsPage(driver=login_page.driver)
        assert products_page.is_url_product(), 'Página incorreta!'
        assert products_page.has_title_products(), 'Página incorreta!'
        # finding a list of webelement items
        try:
            inventory_list = products_page.find_all_elements()
        except NoSuchElementException:
            pytest.fail('Lista de produtos indisponível.')
        product_selected = products_page.select_random_product_to_cart(inventory_list)
        product_selected_title = products_page.get_product_title()
        assert products_page.product_is_in_cart(product_selected), 'Produto não adicionado ao carrinho!'
        assert products_page.cart_icon_is_1(), 'Produto não adicionado ao carrinho!'
        cart_page = YourCartPage(driver=products_page.go_to_cart())
        assert cart_page.is_url_cart(), 'Página incorreta!'
        assert cart_page.cart_has_product_for_checkout(
            product_selected_title), "Produto selecionado não está no carrinho!"

        checkout_page_part_one = CheckoutOnePage(driver=cart_page.go_to_checkout())
        assert checkout_page_part_one.is_url_checkout_one(), 'Página incorreta!'
        checkout_page_part_two = CheckoutTwoPage(driver=checkout_page_part_one.go_to_checkout_two())
        assert checkout_page_part_two.is_url_checkout_two(), 'Página incorreta!'
        assert checkout_page_part_two.product_summary_is_correct(
            product_selected_title), 'Produto selecionado não está no checkout!'
        checkout_page_finish = CheckoutFinishPage(driver=checkout_page_part_two.go_to_finish())
        assert checkout_page_finish.is_url_checkout_completed(), 'Página incorreta!'
        assert checkout_page_finish.is_checkout_completed(), 'Checkout não foi completado com sucesso.'
