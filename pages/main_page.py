from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'signup-button.header-button.abcmouse-sans.enteractive.tab-outline-blue')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'signup-button.header-button.abcmouse-sans.enteractive.tab-outline-blue')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'signup-button.header-button.abcmouse-sans.enteractive.tab-outline-blue')
    BECOME_A_MEMBER_TEXT = (By.CSS_SELECTOR, 'signup-button.header-button.abcmouse-sans.enteractive.tab-outline-blue')

    def open_main_page(self):
        self.open_url('https://www.abcmouse.com')

    def click_sign_up_button(self):
        self.click(*self.SIGN_UP_BUTTON)

    def verify_url_contains_query(self, query):
        self.verify_url_contains_query(query)

    def input_email(self, email):
        self.input_text(email, *self.EMAIL_FIELD)

    def click_submit_button(self):
        self.click(*self.SUBMIT_BUTTON)

    def verify_become_a_member_text(self, result_word):
        self.verify_text(result_word, *self.BECOME_A_MEMBER_TEXT)