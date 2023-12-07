from pages.MenuPage import MenuPage


class Test3:

    def test_logout(self, login_saucedemo):
        login_page = login_saucedemo
        menu_page = MenuPage(driver=login_page.driver)
        menu_page.open_menu()
        assert menu_page.is_menu_open(), 'Erro no carregamento: menu não exibido.'
        menu_page.click_logout()
        assert login_page.is_url_login(), 'Página incorreta!'
