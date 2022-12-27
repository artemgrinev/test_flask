import allure

from locators.page_elements import PageLocators
from pages.base_page import BasePage


class PageElements(BasePage):
    _locator = PageLocators()

    @allure.step("Getting body text")
    def get_body_text(self) -> str:
        body_text = self.element_is_visible(self._locator.BODY_TEXT).text
        return body_text

    @allure.step("Getting background color page")
    def get_color_bg(self) -> str:
        color_bg = self.element_is_present(self._locator.SECTION).value_of_css_property('background-color')
        return color_bg

    @allure.step("Getting text and link buttons")
    def check_button(self, button: str) -> tuple:
        buttons = {
                    "home": {
                            'text_btn': self.element_is_visible(self._locator.HOME_BUTTON).text,
                            'link_btn': self.element_is_visible(self._locator.HOME_BUTTON).get_property("href")
                            },
                    "login": {
                            'text_btn': self.element_is_visible(self._locator.LOGIN_BUTTON).text,
                            'link_btn': self.element_is_visible(self._locator.LOGIN_BUTTON).get_property("href")
                            },
                    "signup": {
                            'text_btn': self.element_is_visible(self._locator.SIGNUP_BUTTON).text,
                            'link_btn': self.element_is_visible(self._locator.SIGNUP_BUTTON).get_property("href")
                            },
                    "profile": {
                        'text_btn': self.element_is_visible(self._locator.PROFILE_BUTTON).text,
                        'link_btn': self.element_is_visible(self._locator.PROFILE_BUTTON).get_property("href")
                    },
                    "logout": {
                        'text_btn': self.element_is_visible(self._locator.LOGOUT_BUTTON).text,
                        'link_btn': self.element_is_visible(self._locator.LOGOUT_BUTTON).get_property("href")
                    },
                    }
        return buttons[button]['text_btn'], buttons[button]['link_btn']

    @allure.step("Checking click nav bar button")
    def check_click_navbar_buttons(self, button: str) -> str:
        buttons = {
                    "home": self.element_is_visible(self._locator.HOME_BUTTON),
                    "login": self.element_is_visible(self._locator.LOGIN_BUTTON),
                    "signup": self.element_is_visible(self._locator.SIGNUP_BUTTON),
                    "profile": self.element_is_visible(self._locator.PROFILE_BUTTON),
                    "logout": self.element_is_visible(self._locator.LOGOUT_BUTTON),
                  }
        with allure.step('click button'):
            buttons.get(button).click()
        with allure.step('getting url opened page'):
            url = self._driver.current_url
        return url

