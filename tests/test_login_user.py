import allure
import pytest

from data.valid_data import PageUrls, LoginPageData, PagesData
from pages.login_page import Login
from pages.page_elements import PageElements


@allure.suite("Login user")
class TestLogin:
    url = "http://localhost:5000/login"

    @allure.feature('EULP-1 Filling valid data out all fields')
    def test_login_valid_user(self, driver, get_users):
        page = Login(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        email = get_users[0]['field_data'][0]
        password = get_users[0]['field_data'][1]
        page.fill_text_fields_login(email, password)
        url_open_page = page.click_login_button()
        assert url_open_page == PageUrls.PROFILE_URL

    @allure.feature('EULN-1 Register user with all empty fields')
    def test_login_empty_field(self, driver):
        page = Login(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        email, name, password = '', '', ''
        page.fill_text_fields_login(email, name, password, all_fields=True)
        url_open_page = page.click_login_button()
        assert url_open_page == PageUrls.LOGIN_URL, 'login user fill empty field'

    @allure.feature('EULN-2 Existing user login with wrong password')
    def test_login_wrong_password(self, driver, get_users):
        page = Login(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        not_valid_email = get_users[0]['field_data'][0]
        password = get_users[0]['field_data'][1][1:]
        page.fill_text_fields_login(not_valid_email, password)
        page.click_login_button()
        alert_text = page.check_alert_text()
        assert alert_text == LoginPageData.alert_text

    @allure.feature('EULN-3 Non-existent user login')
    def test_non_existent_user_login(self, driver, get_users):
        page = Login(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        not_valid_email = get_users[0]['field_data'][0][1:]
        password = get_users[0]['field_data'][1]
        page.fill_text_fields_login(not_valid_email, password)
        page.click_login_button()
        alert_text = page.check_alert_text()
        assert alert_text == LoginPageData.alert_text


@allure.suite("Test login page")
class TestLoginPage:
    url = "http://localhost:5000/login"

    @pytest.mark.parametrize("width, height", [('1920', '1080'), ('768', '1024'), ('360', '640')])
    @allure.feature('step-2.3 Getting body text')
    def test_open_page(self, driver, width, height):
        driver.set_window_size(width, height)
        page = PageElements(driver, self.url)
        page.open()
        body_text = page.get_body_text()
        bg_color = page.get_color_bg()
        assert body_text == PagesData.BODY_TEXT_LOGIN, 'Body text is not correct'
        assert bg_color == PagesData.BG_COLOR, 'Background-color is not correct'

    @pytest.mark.parametrize("width, height", [('1920', '1080'), ('768', '1024'), ('360', '640')])
    @allure.feature('step-2.1 Check nav bar buttons')
    def test_nav_bar_buttons(self, driver, width, height):
        driver.set_window_size(width, height)
        page = PageElements(driver, self.url)
        page.open()
        home_text_btn, home_link_btn = page.check_button("home")
        login_text_btn, login_link_btn = page.check_button("login")
        signup_text_btn, signup_link_btn = page.check_button("signup")
        assert home_text_btn == PagesData.HOME_BTN_TEXT, 'Home button text is not correct'
        assert home_link_btn == PageUrls.HOME_URL, 'Home button link is not correct'
        assert login_link_btn == PageUrls.LOGIN_URL, 'Login button text is not correct'
        assert login_text_btn == PagesData.LOGIN_BTN_TEXT, 'Login button link is not correct'
        assert signup_text_btn == PagesData.SIGNUP_BTN_TEXT, 'Sign Up button text is not correct'
        assert signup_link_btn == PageUrls.SIGNUP_URL, 'Sign Up button link is not correct'

    @allure.feature('step-2.2 Click nav-menu button')
    @pytest.mark.parametrize("width, height", [('1920', '1080'), ('768', '1024'), ('360', '640')])
    @pytest.mark.parametrize("button, check_url", [('signup', PageUrls.SIGNUP_URL),
                                                   ('home', PageUrls.HOME_URL),
                                                   ('login', PageUrls.LOGIN_URL)])
    def test_click_signup_button(self, driver, width, height, button, check_url):
        with allure.step(f'click {button} ,browser size: {width}x{height}'):
            driver.set_window_size(width, height)
            page = PageElements(driver, self.url)
            page.open()
            url = page.check_click_navbar_buttons(button)
            assert url == check_url, 'Wrong page opened after clicking'
