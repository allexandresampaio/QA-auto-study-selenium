# using the initial tests as a single test inside class
class HomepageTests:

    # following, the example for when using a different name for setup
    # def test_click_login_button(self, setup_name):
    def test_check_basic_info(self, open_browser):
        home_page = open_browser
        home_page.click_login_button()

        # test that after button click, page does not change (url is the same)
        assert home_page.is_url_login(), 'Página incorreta!'

        # test that after button click, error message is shown on screen
        assert home_page.has_login_error_message(), 'Mensagem de erro inválida!'
