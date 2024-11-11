from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_project.config import timeout

class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.home_page_label = (By.XPATH, "//h1[@id='title' and contains(., 'UI Test Automation')]")
    
    def home_page_is_opened(self):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.home_page_label)
            )
            return True
        except Exception as e:
            print(f"Ошибка при проверке главной страницы: {e}")
            return False
        
    def open_page(self, page_name):
        page_selector = (By.LINK_TEXT, page_name)
        
        try:
            self.driver.find_element(*page_selector).click()
            print(f"Открыта страница: {page_name}")
        except Exception as e:
            print(f"Ошибка при открытии страницы {page_name}: {e}")
