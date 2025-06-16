import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.text_input.page_text_input import TextInputPage
from pages.text_input.page_email_field import EmailFieldPage
from pages.text_input.page_password_field import PasswordFieldPage

@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def text_input_page(browser):
    driver = browser
    driver.delete_all_cookies()
    page = TextInputPage(driver)
    page.open_page()
    yield page


@pytest.fixture
def email_field_page(browser):
    driver = browser
    driver.delete_all_cookies()
    page = EmailFieldPage(driver)
    page.open_page()
    yield page


@pytest.fixture
def password_field_page(browser):
    driver = browser
    driver.delete_all_cookies()
    page = PasswordFieldPage(driver)
    page.open_page()
    yield page