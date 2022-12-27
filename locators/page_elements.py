from selenium.webdriver.common.by import By


class PageLocators:
    SECTION = (By.CSS_SELECTOR, "section")
    BODY_TEXT = (By.CSS_SELECTOR, "div[class='hero-body'] h1")
    NAV_BAR = "div[class='navbar-menu']"
    HOME_BUTTON = (By.CSS_SELECTOR, "div[class='navbar-end'] :nth-child(1)")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "div[class='navbar-end'] :nth-child(2)")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "div[class='navbar-end'] :nth-child(3)")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "div[class='navbar-end'] :nth-child(2)")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "div[class='navbar-end'] :nth-child(3)")

