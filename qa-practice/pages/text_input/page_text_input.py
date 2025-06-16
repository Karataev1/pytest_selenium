from pages.text_input.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from pages.text_input.selectors import TextInputSelectors as TISelectors



class TextInputPage(BasePage):
    def __init__(self,browser: WebDriver):
        super().__init__(browser)
        self.page_url = 'https://www.qa-practice.com/elements/input/simple'


    def input_text_line(self) -> WebElement:
        return self.find(TISelectors.input_text_line,timeout=5)


    def error_message(self) -> WebElement:
        return self.find(TISelectors.error_message,timeout=5)


    def result(self) -> WebElement:
        return self.find(TISelectors.result,timeout=5)


    def get_result_text(self) -> str:
        return self.result().text


    def get_error_message_text(self) -> str:
        return self.error_message().text


    def input_line_is_displayed(self) -> bool:
        return self.input_text_line().is_displayed()


    def input_line_is_enabled(self) -> bool:
        return self.input_text_line().is_enabled()


    def text_line_set_text(self,text: str) -> 'TextInputPage':
        self.input_text_line().send_keys(text)
        return self


    def clear_text_line(self) -> 'TextInputPage':
        self.input_text_line().clear()
        return self


    def press_enter_in_line(self) -> 'TextInputPage':
        self.input_text_line().click()
        self.input_text_line().send_keys(Keys.ENTER)
        return self