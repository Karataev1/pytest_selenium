import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.text_input.text_input import TextInput
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="session")
def browser():
    options = Options()
    #options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    yield driver, wait
    driver.quit()


@pytest.fixture
def text_input_page(browser):
    driver, wait = browser
    driver.delete_all_cookies()
    page = TextInput(driver, wait)
    page.open()
    yield page