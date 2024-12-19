import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_logs.log"),
        logging.StreamHandler()
    ]
)

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def wait_for_element_visibility(self, locator):
        try:
            self.logger.info(f"Ожидание видимости элемента: {locator}")
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
        )
        except TimeoutException as e:
            self.logger.error(f"Элемент {locator} не появился за {self.timeout} секунд: {e}")
            return None

    def click_element(self, locator):
        try:
            element = self.wait_for_element_visibility(locator)
            if element:
                element.click()
                self.logger.info(f"Клик выполнен по элементу: {locator}")
                return True
        except Exception as e:
            self.logger.error(f"Ошибка при клике на элемент {locator}: {e}")
        return False
    
    def enter_text(self, locator, text):
        try:
            element = self.wait_for_element_visibility(locator)
            if element:
                element.clear()
                element.send_keys(text)
                self.logger.info(f"Текст '{text}' успешно введён в элемент: {locator}")
                return text
            else:
                self.logger.warning(f"Элемент {locator} не найден для ввода текста.")
        except Exception as e:
            self.logger.error(f"Ошибка при вводе текста в элемент {locator}: {e}")
            return False

    def open_page(self, locator):
        try:
            element = self.wait_for_element_visibility(locator)
            if element:
                element.click()
                self.logger.info(f"Страница '{locator}' успешно открыта.")
                return True
            else:
                self.logger.warning(f"Элемент для страницы '{locator}' не найден.")
        except Exception as e:
            self.logger.error(f"Ошибка при открытии страницы '{locator}': {e}")
            return False
        
    def get_text(self, locator):
        try:
            element = self.wait_for_element_visibility(locator)
            if element:
                return element.text
            else:
                self.logger.warning(f"Элемент для страницы '{locator}' не найден.")
        except Exception as e:
            self.logger.error(f"Ошибка при открытии страницы '{locator}': {e}")
            return False
