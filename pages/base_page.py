from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def open_url(self, url,):
        self.driver.get(url)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)
        print(f'Inputting text: {text}')

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Error. Expected {expected_text}, but got {actual_text}'

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(*locator), message=f'Element not clickable by {locator}')
        e.click()



    def verify_element_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Checking by locator {locator}. Expected {expected_text}, but got {actual_text}'


    def verify_url_contains_query(self, query):
        self.wait.until(EC.url_contains(query))