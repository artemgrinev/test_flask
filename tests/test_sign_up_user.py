import allure
import pytest

from data.valid_data import PageUrls, PagesData
from pages.page_elements import PageElements
from pages.sign_up_page import SignUpPage
from data.not_valid_data import not_valid_email, not_valid_password, not_valid_name


@allure.suite("Registration users")
class TestSignUp:
    url = "http://localhost:5000/signup"

    @allure.feature('GNUN-4 Register user with all empty fields')
    def test_sign_up_empty_field(self, driver):
        page = SignUpPage(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        email, name, password = '', '', ''
        data = page.fill_text_fields(email, name, password, all_fields=True)
        data = page.click_signup_button(data)
        assert data['url_opened_page'] == PageUrls.LOGIN_URL

    @allure.feature('CNUP-1 Filling valid data out all fields')
    def test_sign_up_all_field(self, driver, generated_valid_data, writing_data, create_connection_db):
        page = SignUpPage(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        email, name, password = generated_valid_data
        data = page.fill_text_fields(email, name, password, all_fields=True)
        data = page.click_signup_button(data)
        assert data['field_data'] == data['generated_data']
        assert data['url_opened_page'] == PageUrls.LOGIN_URL
        assert email == create_connection_db('email', email)
        writing_data(data)

    @allure.feature('GNUP-2 Filling valid data in only required fields')
    def test_sign_up_only_required_field(self, driver, generated_valid_data, writing_data):
        page = SignUpPage(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        email, name, password = generated_valid_data
        data = page.fill_text_fields(email, name, password, all_fields=False)
        data = page.click_signup_button(data)
        assert data['field_data'] == data['generated_data']
        assert data['url_opened_page'] == PageUrls.LOGIN_URL
        writing_data(data)

    @pytest.mark.parametrize("fild, value", [('email', not_valid_email),
                                             ('name', not_valid_name),
                                             ('password', not_valid_password)])
    @allure.feature('GNUN-1,2,3 Filling not valid data')
    def test_sign_up_not_valid_data(self, driver, fild, value, generated_valid_data):
        page = SignUpPage(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        email, name, password = generated_valid_data
        for fild in value:
            data = page.fill_text_fields(email, name, password, all_fields=True)
            data = page.click_signup_button(data)
            assert data['url_opened_page'] == PageUrls.SIGNUP_URL, f"Registered with incorrect email: {fild}"

    @allure.feature('GNUP-3 Registration and login in different windows')
    def test_signup_and_login_from_different_windows(self, driver, generated_valid_data, writing_data):
        page = SignUpPage(driver, self.url)
        with allure.step(f"step-1 open page {self.url}"):
            page.open()
        email, name, password = generated_valid_data
        data = page.fill_text_fields(email, name, password, all_fields=True)
        page.click_signup_button(data)
        page.open_new_window(PageUrls.LOGIN_URL)
        url_page = page.fill_text_fields_login(email, password)
        assert url_page == PageUrls.PROFILE_URL


@allure.suite("Test Sign up page")
class TestSignUpPage:
    url = "http://localhost:5000/signup"

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

    @pytest.mark.parametrize("width, height", [('1920', '1080'), ('768', '1024'), ('360', '640')])
    @allure.feature('step-2.3 getting body text')
    def test_open_page(self, driver, width, height):
        driver.set_window_size(width, height)
        page = PageElements(driver, self.url)
        page.open()
        body_text = page.get_body_text()
        bg_color = page.get_color_bg()
        assert body_text == PagesData.BODY_TEXT_HOME, 'Body text is not correct'
        assert bg_color == PagesData.BG_COLOR, 'Background-color is not correct'
