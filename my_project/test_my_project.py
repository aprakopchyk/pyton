import pytest
from my_project.pages.home_page import HomePage
from my_project.pages.input_page import InputPage
from my_project.pages.sample_page import SamplePage
from my_project.test_data import *
from my_project.config import *
from selenium import webdriver

@pytest.fixture

def setup():
    driver = webdriver.Chrome()  
    driver.get(base_url)
    home_page = HomePage(driver)
    assert home_page.home_page_is_opened()
    yield driver
    driver.quit()

def test_text_on_button(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.open_page('Text Input')
    input_page = InputPage(driver)
    assert input_page.input_page_is_opened()
    random_text = input_page.enter_random_text()
    input_page.click_button()
    button_text = input_page.get_text_from_button()
    assert button_text == random_text

def test_welcome_message(setup):
    driver = setup
    home_page = HomePage(driver)
    home_page.open_page('Sample App')
    sample_page = SamplePage(driver)
    assert sample_page.sample_page_is_opened()
    test_username = sample_page.enter_random_username()
    sample_page.enter_password(password)
    sample_page.click_button()
    welcome_text = sample_page.get_success_message()
    assert test_username in welcome_text