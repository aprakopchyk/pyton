from selenium.webdriver.common.by import By
from my_project.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.home_page_label = (By.XPATH, "//h1[@id='title' and contains(., 'UI Test Automation')]")
    
    def home_page_is_opened(self):
        return self.wait_for_element_visibility(self.home_page_label) is not None
        
    def open_page(self, page_name):
        page_selector = (By.LINK_TEXT, page_name)
        return super().open_page(page_selector)
