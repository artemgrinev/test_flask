import random

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self, driver: WebDriver, url: str):
        self._driver = driver
        self._url = url

    def open(self):
        self._driver.get(self._url)

    def element_is_visible(self, locator: tuple, timeout=5) -> WebElement:  # Если необходимо чтобы элемент был видимым
        return wait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_visible(self, locator: tuple, timeout=5) -> list[WebElement]:  # Если необходимо чтобы все элементы были видимыми
        return wait(self._driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator: tuple, timeout=5) -> WebElement: # Если необходимо проверить присутствия элемента в DOM.
        return wait(self._driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_present(self, locator: tuple, timeout=5) -> list[WebElement]: # Если необходимо проверить присутствия элементов в DOM.
        return wait(self._driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def go_to_element(self, element: WebElement):  # проскролить к искомому элементу
        self._driver.execute_script("arguments[0].scrollIntoView();", element)

    def element_is_clickable(self, locator: tuple, timeout=5) -> WebElement:  # Чтобы элемент был кликабельным.
        return wait(self._driver, timeout).until(EC.element_to_be_clickable(locator))

    def double_click_action(self, element: WebElement):
        actions = ActionChains(self._driver)
        actions.double_click(element)
        actions.perform()

    def right_click_action(self, element: WebElement):
        actions = ActionChains(self._driver)
        actions.context_click(element)
        actions.perform()

    def click_to_element(self, element: WebElement):
        actions = ActionChains(self._driver)
        actions.move_to_element(element).click()
        actions.perform()

    def click_to_enter(self):
        actions = ActionChains(self._driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def click_to_arrow_down(self):
        actions = ActionChains(self._driver)
        for i in range(random.randint(3, 20)):
            actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()

    def remove_ads(self):
        self._driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self._driver.execute_script("document.getElementById('fixedban').remove();")

    def set_element_by_visible_text(self, element: tuple, value: str):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)