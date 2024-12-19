from selenium.webdriver.common.by import By
from my_project.pages.base_page import BasePage

class InputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.input_page_label = (By.XPATH, "//h3[contains(text(), 'Text Input')]")
        self.input = (By.ID, "newButtonName")
        self.button = (By.ID, "updatingButton")
    
    def input_page_is_opened(self):
        return self.wait_for_element_visibility(self.input_page_label) is not None
        
    def enter_text(self, text):
        return super().enter_text(self.input, text)

    def click_button(self):
        return self.click_element(self.button)

    def get_text_from_button(self):
        return self.get_text(self.button)