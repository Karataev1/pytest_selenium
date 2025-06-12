from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.text_input.text_input import TextInput
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pytest
import re
import string

invalid_number_26 = '12345678910111213141516171'
INVALID_CHARACTERS = list((string.punctuation.replace("-", "").replace("_", "")))


@pytest.fixture
def browser_fixture():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options)
    page = TextInput(browser)
    page.open()
    yield page
    browser.quit()


def test_line_is_displayed(browser_fixture):
    assert browser_fixture.input_text_line().is_displayed()


def test_line_is_enabled(browser_fixture):
    assert browser_fixture.input_text_line().is_enabled()


@pytest.mark.parametrize("invalid_string", INVALID_CHARACTERS)
def test_invalid_characters_in_input(browser_fixture, invalid_string):
    browser_fixture.input_text_line().clear()
    browser_fixture.input_text_line().send_keys(invalid_string + 'test')
    browser_fixture.input_text_line().send_keys(Keys.ENTER)

    assert browser_fixture.error_message() == 'Enter a valid string consisting of letters, numbers, underscores or hyphens.'


def test_send_text(browser_fixture,text='ok123_-AA'):
    browser_fixture.input_text_line().send_keys(text)
    browser_fixture.input_text_line().send_keys(Keys.ENTER)
    assert browser_fixture.result_text() == text


@pytest.mark.parametrize('invalid_number_of_character',['1',invalid_number_26])
def test_invalid_number_of_characters(browser_fixture,invalid_number_of_character):
    browser_fixture.input_text_line().send_keys(invalid_number_of_character)
    browser_fixture.input_text_line().send_keys(Keys.ENTER)
    assert (browser_fixture.error_message() == 'Please enter 2 or more characters' or
            browser_fixture.error_message() == 'Please enter no more than 25 characters')


