# using the initial tests as a single test inside class
class Test1:

    # creating the first test
    # following, the example for when using a different name for setup
    # def test_click_login_button(self, setup_name):
    def test_click_login_button(self, open_browser):
        login_page = open_browser
        login_page.click_login_button()

        # test that after button click, page does not change (url is the same)
        assert login_page.is_url_login(), 'Página incorreta!'

        # test that after button click, error message is shown on screen
        assert login_page.has_login_error_message(), 'Mensagem de erro inválida!'
