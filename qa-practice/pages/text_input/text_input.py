from selenium.webdriver.common.by import By
from pages.text_input.base_page import BasePage
from selenium.webdriver.common.keys import Keys

selector_input_text_line = (By.ID, 'id_text_string')
selector_result_text = (By.ID, 'result-text')
selector_error_message = (By.ID, 'error_1_id_text_string')

class TextInput(BasePage):
    def __init__(self,browser):
        super().__init__(browser)


    def open(self):
        return self.browser.get('https://www.qa-practice.com/elements/input/simple')


    def input_text_line(self):
        return self.find(selector_input_text_line)


    def result_text(self):
        return self.find(selector_result_text).text


    def press_enter(self):
        self.find(selector_input_text_line).send_keys(Keys.ENTER)
        return self.find(selector_input_text_line)


    def error_message(self):
        return self.find(selector_error_message).text