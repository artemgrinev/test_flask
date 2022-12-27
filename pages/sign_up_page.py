import allure

from locators.sign_up_page_locators import SignUpLocators
from pages.base_page import BasePage


class SignUpPage(BasePage):
    _locator = SignUpLocators()

    @allure.step("step-2.1 Fill text fields")
    def fill_text_fields(self, email: str, name: str, password: str,  all_fields=True):
        name_fields = self.element_is_visible(self._locator.INPUT_NAME)
        email_fields = self.element_is_visible(self._locator.INPUT_EMAIL)
        password_fields = self.element_is_visible(self._locator.INPUT_PASSWORD)
        data = {'field_data': [],
                'generated_data': [],
                'url_opened_page': ''}
        if all_fields:
            with allure.step("filing valid data all fields"):
                name_fields.send_keys(name)
                email_fields.send_keys(email)
                password_fields.send_keys(password)
                field_name_text = name_fields.get_attribute('value')
                field_email_text = email_fields.get_attribute('value')
                field_password_text = password_fields.get_attribute('value')
                data["field_data"] = [field_email_text, field_name_text, field_password_text]
                data['generated_data'] = [email, name, password]
        else:
            with allure.step("filing valid data required fields"):
                email_fields.send_keys(email)
                password_fields.send_keys(password)
                field_email_text = email_fields.get_attribute('value')
                field_password_text = password_fields.get_attribute('value')
                data['field_data'] = [field_email_text, field_password_text]
                data['generated_data'] = [email, password]
        return data

    @allure.step("step-2.2 click sign up button")
    def click_signup_button(self, data: dict) -> dict:
        self.element_is_visible(self._locator.SIGN_UP_BUTTON).click()
        data['url_opened_page'] = self._driver.current_url
        return data

    @allure.step("step-3 Open new window")
    def open_new_window(self, url):
        self._driver.execute_script(f"window.open('{url}')")
        self._driver.switch_to.window(self._driver.window_handles[1])

    @allure.step("step-3 filling in text fields on the registration page")
    def fill_text_fields_login(self, email: str, password: str) -> str:
        email_fields = self.element_is_visible(self._locator.INPUT_EMAIL)
        password_fields = self.element_is_visible(self._locator.INPUT_PASSWORD)
        email_fields.send_keys(email)
        password_fields.send_keys(password)
        with allure.step('step-3.1 click login button'):
            self.element_is_visible(self._locator.LOGIN_BUTTON).click()
        return self._driver.current_url
