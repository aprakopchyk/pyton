from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_project.test_data import *
from my_project.config import timeout
import random, string 

class SamplePage:
    def __init__(self, driver):
        self.driver = driver

        self.sample_page_label = (By.XPATH, "//h3[contains(text(), 'Sample App')]")
        self.username_input = (By.CSS_SELECTOR, "input[type='text']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.button = (By.ID, "login")
        self.success_message = (By.ID, "loginstatus")

    def sample_page_is_opened(self):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.sample_page_label)
            )
            return True
        except Exception as e:
            print(f"Ошибка при проверке главной страницы: {e}")
            return False

    def enter_random_username(self, length = 10):
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        username_input = self.driver.find_element(*self.username_input)
        username_input.clear()
        username_input.send_keys(random_text)   
        print(f"Введен текст: {random_text}")
        return random_text

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_input)
        password_input.clear()
        password_input.send_keys(password)

        print(f"Введен пароль: {password}")
    
    def click_button(self):
        try:
            button_element = self.driver.find_element(*self.button)
            button_element.click()
            print("Кнопка была нажата")
        except Exception as e:
            print(f"Ошибка при клике по кнопке: {e}")

    def get_success_message(self): 
        try:
            welcome_message = self.driver.find_element(*self.success_message).text
            print(f"Текст на кнопке: {welcome_message}")
            return welcome_message
        except Exception as e:
            print(f"Ошибка при получении текста с кнопки: {e}")
            return None