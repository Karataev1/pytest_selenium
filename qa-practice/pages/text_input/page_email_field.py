from pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from pages.text_input.selectors import TextInputSelectors as TISelectors



class EmailFieldPage(BasePage):
    def __init__(self,browser: WebDriver):
        super().__init__(browser)
        self.page_url = 'https://www.qa-practice.com/elements/input/email'


    def email_input_line(self) -> WebElement:
        return self.find(TISelectors.email_input_line,timeout=5)


    def error_message(self) -> WebElement:
        return self.find(TISelectors.email_error_message,timeout=5)


    def result(self) -> WebElement:
        return self.find(TISelectors.result,timeout=5)


    def get_result_text(self) -> str:
        return self.result().text


    def get_error_message_text(self) -> str:
        return self.error_message().text


    def email_input_line_is_displayed(self) -> bool:
        return self.email_input_line().is_displayed()


    def email_input_line_is_enabled(self) -> bool:
        return self.email_input_line().is_enabled()


    def email_input_line_set_text(self,text: str) -> 'EmailFieldPage':
        self.email_input_line().send_keys(text)
        return self


    def clear_text_line(self) -> 'EmailFieldPage':
        self.email_input_line().clear()
        return self


    def press_enter_in_line(self) -> 'EmailFieldPage':
        self.email_input_line().click()
        self.email_input_line().send_keys(Keys.ENTER)
        return self