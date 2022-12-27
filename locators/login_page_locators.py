from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "form[action='/login'] button")

    SECTION = (By.CSS_SELECTOR, "section")
    BODY_TEXT = (By.CSS_SELECTOR, "div[class='hero-body'] h1")
    NAV_BAR = "div[class='navbar-menu']"
    HOME_NAVBAR_BUTTON = (By.CSS_SELECTOR, "div[class='navbar-end'] :nth-child(1)")
    LOGIN_NAVBAR_BUTTON = (By.CSS_SELECTOR, "div[class='navbar-end'] :nth-child(2)")
    SIGNUP_NAVBAR_BUTTON = (By.CSS_SELECTOR, "div[class='navbar-end'] :nth-child(3)")
    ALERT = (By.CSS_SELECTOR, "div[class='notification is-danger']")
