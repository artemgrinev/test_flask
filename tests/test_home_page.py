import allure
import pytest

from pages.page_elements import PageElements
from data.valid_data import PageUrls, PagesData


@allure.suite("Test Home Page")
class TestHomePage:
    url = "http://localhost:5000"

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
    @allure.feature('step-2.3 Getting body text')
    def test_open_page(self, driver, width, height):
        driver.set_window_size(width, height)
        page = PageElements(driver, self.url)
        page.open()
        body_text = page.get_body_text()
        bg_color = page.get_color_bg()
        assert body_text == PagesData.BODY_TEXT_HOME, 'Body text is not correct'
        assert bg_color == PagesData.BG_COLOR, 'Background-color is not correct'



