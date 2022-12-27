import allure
import pytest

from data.valid_data import PagesData, PageUrls
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.page_elements import PageElements


class Login(BasePage):
    _locator = LoginPageLocators()

    @allure.step("step-2.1 filling in text fields")
    def fill_text_fields_login(self, email: str, password: str):
        with allure.step('filling fields'):
            self.element_is_visible(self._locator.INPUT_EMAIL).send_keys(email)
            self.element_is_visible(self._locator.INPUT_PASSWORD).send_keys(password)

    @allure.step("step-2.2 click login button")
    def click_login_button(self) -> str:
        self.element_is_visible(self._locator.LOGIN_BUTTON).click()
        return self._driver.current_url

    @allure.step("check alert text")
    def check_alert_text(self) -> str:
        text = self.element_is_visible(self._locator.ALERT).text
        return text


@allure.suite("OP-2 Test Login page")
class TestSignUpPage:
    url = "http://localhost:5000/login"

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
        assert home_link_btn == PagesData.HOME_BTN_LINK, 'Home button link is not correct'
        assert login_link_btn == PagesData.LOGIN_BTN_LINK, 'Login button text is not correct'
        assert login_text_btn == PagesData.LOGIN_BTN_TEXT, 'Login button link is not correct'
        assert signup_text_btn == PagesData.SIGNUP_BTN_TEXT, 'Sign Up button text is not correct'
        assert signup_link_btn == PagesData.SIGNUP_BTN_LINK, 'Sign Up button link is not correct'

    @allure.feature('step-2.2 Click nav-menu button')
    @pytest.mark.parametrize("width, height", [('1920', '1080'), ('768', '1024'), ('360', '640')])
    @pytest.mark.parametrize("button, check_url", [('signup', PageUrls.SIGNUP_URL),
                                                   ('home', PageUrls.HOME_URL),
                                                   ('login', PageUrls.LOGIN_URL)])
    def test_click_navbar_button(self, driver, width, height, button, check_url):
        with allure.step(f'click {button} ,browser size: {width}x{height}'):
            driver.set_window_size(width, height)
            page = PageElements(driver, self.url)
            page.open()
            url = page.check_click_navbar_buttons(button)
            assert url == check_url, 'Wrong page opened after clicking'
