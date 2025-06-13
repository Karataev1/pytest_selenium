from selenium.webdriver.common.by import By


class TextInputSelectors:

    @staticmethod
    def input_text_line():
        return By.ID, 'id_text_string'


    @staticmethod
    def result():
        return By.ID, 'result-text'


    @staticmethod
    def error_message():
        return By.ID, 'error_1_id_text_string'
