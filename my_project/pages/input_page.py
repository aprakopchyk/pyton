from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_project.config import timeout
import random, string

class InputPage:
    def __init__(self, driver):
        self.driver = driver

        self.input_page_label = (By.XPATH, "//h3[contains(text(), 'Text Input')]")
        self.input = (By.ID, "newButtonName")
        self.button = (By.ID, "updatingButton")
    
    def input_page_is_opened(self):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.input_page_label)
            )
            return True
        except Exception as e:
            print(f"Ошибка при проверке главной страницы: {e}")
            return False
        
    def enter_random_text(self, length=10):
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        input_element = self.driver.find_element(*self.input)
        input_element.clear()
        input_element.send_keys(random_text)
        print(f"Введен текст: {random_text}")
        return random_text

    def click_button(self):
        try:
            button_element = self.driver.find_element(*self.button)
            button_element.click()
            print("Кнопка была нажата")
        except Exception as e:
            print(f"Ошибка при клике по кнопке: {e}")

    def get_text_from_button(self):
        try:
            button_text = self.driver.find_element(*self.button).text
            print(f"Текст на кнопке: {button_text}")
            return button_text
        except Exception as e:
            print(f"Ошибка при получении текста с кнопки: {e}")
            return None