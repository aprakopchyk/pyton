from selenium.webdriver.common.by import By
from my_project.test_data import *
from my_project.pages.base_page import BasePage

class SamplePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.sample_page_label = (By.XPATH, "//h3[contains(text(), 'Sample App')]")
        self.username_input = (By.CSS_SELECTOR, "input[type='text']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.button = (By.ID, "login")
        self.success_message = (By.ID, "loginstatus")

    def sample_page_is_opened(self):
        return self.wait_for_element_visibility(self.sample_page_label) is not None

    def enter_username(self, text):
        return self.enter_text(self.username_input, text)

    def enter_password(self, password):
        return self.enter_text(self.password_input, password)
    
    def click_button(self):
        return self.click_element(self.button)

    def get_success_message(self): 
        return self.get_text(self.success_message)