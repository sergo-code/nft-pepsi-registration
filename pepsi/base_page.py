from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def select_element(self, elem, item='USA'):
        select = Select(elem)
        select.select_by_value(item)

    def scroll_to_element(self, elem):
        return self.driver.execute_script("return arguments[0].scrollIntoView(true);", elem)

    def go_to_site(self, url):
        return self.driver.get(url)