from pages.MenuPage import MenuPage
from pages.ProductsPage import ProductsPage


class Test2:

    def test_login(self, open_browser):
        login_page = open_browser
        login_page.enter_login()

        products_page = ProductsPage(driver=login_page.driver)

        assert products_page.is_url_product(), 'Página incorreta!'

        assert products_page.has_title_products(), 'Página incorreta!'

        menu_page = MenuPage(driver=products_page.driver)
        assert menu_page.has_menu(), 'Erro no carregamento: menu não exibido.'
