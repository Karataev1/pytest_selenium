import pytest
from conftest import text_input_page as page
from services import GenerateText
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.text_input.selectors import TextInputSelectors as TISelectors
import allure


@allure.feature('text_input_1')
class TestInputPage:
    """
    Здесь тестируется первая вкладка страницы Input Text
    """
    @allure.title('test is_displayed')
    def test_line_is_displayed(self,page):
        """
        Тест проверяет отображение поля ввода для пользователя
        """
        with allure.step('Проверяю отображение поля для ввода'):
            assert page.input_line_is_displayed()


    @allure.title('test is_enabled')
    def test_line_is_enabled(self,page):
        """
        Тест проверяет доступность поля ввода для пользователя
        """
        with allure.step('Проверяю доступность для пользователя поля ввода'):
            assert page.input_line_is_enabled()


    @allure.title('test send_text')
    def test_send_text(self,page, text='ok123_-AA'):
        """
        Тест вводит текст за пользователя, который соответсвует требованиям
        """
        with allure.step(f'Отчищаю поле ввода и ввожу свои данные [{text}]'):
            page.clear_text_line().text_line_set_text(text)
            page.press_enter_in_line()
        with allure.step('Ожидаю окошко с результатом ввода, проверяю соответсвие'):
            try:
                page.wait.until(EC.presence_of_element_located(TISelectors.result()))
                assert page.get_result_text() == text
            except TimeoutException:
                assert False, 'Текст не соответсвует выводу (сообщение о выводе не появилось)'


    @allure.title('test invalid_number_of_characters')
    @pytest.mark.negative
    @pytest.mark.parametrize('invalid_number_of_character', ['1', GenerateText.generate_char(26)])
    def test_invalid_number_of_characters(self,page, invalid_number_of_character):
        """
        Тест вводит неверные данные за пользователя, а именно
        запрещеные для этого поля символы (@=+ и др.). Для того чтобы текст прошел условие (не менее 2 символов)
        в строку подставляется слово 'test'
        """
        with allure.step(f'Отчищаю поле ввода и ввожу свои данные [{invalid_number_of_character}]'):
            page.clear_text_line()
            page.text_line_set_text(invalid_number_of_character)
            page.press_enter_in_line()
        with allure.step('Ожидаю сообщение об ошибке'):
            try:
                page.wait.until(EC.presence_of_element_located(TISelectors.error_message()))
                assert (page.get_error_message_text() == 'Please enter 2 or more characters' or
                        page.get_error_message_text() == 'Please enter no more than 25 characters')
            except TimeoutException:
                assert False, 'Текст с ошибкой не отобразился'


    @allure.title('test invalid_characters_in_input')
    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_string", GenerateText.get_invalid_characters())
    def test_invalid_characters_in_input(self,page, invalid_string):
        """
        Тест вводит данные размером в один символ и больше 25, задача - получить ошибку от сайта
        """
        with allure.step(f'Отчищаю поле ввода и ввожу свои данные [{invalid_string}]'):
            page.clear_text_line()
            page.text_line_set_text(invalid_string)
            page.press_enter_in_line()

        with allure.step('Ожидаю сообщение об ошибке'):
            try:
                page.wait.until(EC.presence_of_element_located(TISelectors.error_message()))
                assert page.get_error_message_text() == 'Enter a valid string consisting of letters, numbers, underscores or hyphens.'
            except TimeoutException:
                assert False, 'Текст с ошибкой не отобразился'









