import pytest
from my_project.pages.home_page import HomePage
from my_project.pages.input_page import InputPage
from my_project.pages.sample_page import SamplePage
from my_project.test_data import *
from my_project.config import *
from selenium import webdriver
import allure
from my_project.StringUtils import StringUtils

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(base_url)
    home_page = HomePage(driver)
    assert home_page.home_page_is_opened()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("setup")
@allure.suite("Main Suite")
class TestMainSuite:
    @allure.tag('smoke', 'regression')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.order(2)
    def test_text_on_button_1(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.open_page('Text Input')
        input_page = InputPage(driver)
        assert input_page.input_page_is_opened()
        text = StringUtils.random_text_generation()
        random_text = input_page.enter_text(text)
        input_page.click_button()
        button_text = input_page.get_text_from_button()
        assert button_text == random_text
    
    @pytest.mark.order(1)
    def test_text_on_button_2(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.open_page('Text Input')
        input_page = InputPage(driver)
        assert input_page.input_page_is_opened()
        text = StringUtils.random_text_generation()
        random_text = input_page.enter_text(text)
        input_page.click_button()
        button_text = input_page.get_text_from_button()
        assert button_text == random_text

@allure.suite("Not Main Suite")
class TestNotMainSuite:
    @allure.tag('mat', 'regression')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_welcome_message(self, setup):
        driver = setup
        home_page = HomePage(driver)
        home_page.open_page('Sample App')
        sample_page = SamplePage(driver)
        assert sample_page.sample_page_is_opened()
        text = StringUtils.random_text_generation()
        test_username = sample_page.enter_username(text)
        sample_page.enter_password(password)
        sample_page.click_button()
        welcome_text = sample_page.get_success_message()
        assert test_username in welcome_text