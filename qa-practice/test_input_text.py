import pytest
from conftest import text_input_page as page
from servises.generate_text import GenerateText
from selenium.common.exceptions import TimeoutException
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
            page.take_a_screenshot_in_allure(name='page_screen')
            assert page.input_line_is_displayed()


    @allure.title('test is_enabled')
    def test_line_is_enabled(self,page):
        """
        Тест проверяет доступность поля ввода для пользователя
        """
        with allure.step('Проверяю доступность поля ввода для пользователя'):
            assert page.input_line_is_enabled()


    @allure.title('test send_text')
    def test_send_text(self,page, text='ok123_-AA'):
        """
        Тест вводит текст за пользователя, который соответствует требованиям
        """
        with allure.step(f'Отчищаю поле ввода и ввожу свои данные [{text}]'):
            page.clear_text_line().text_line_set_text(text)
        with allure.step(f'Нажимаю ENTER'):
            page.press_enter_in_line()
        with allure.step('Ожидаю окошко с результатом ввода, проверяю соответствие'):
            try:
                assert page.get_result_text() == text
            except TimeoutException:
                page.take_a_screenshot_in_allure(name='fail_screen')
                assert False, 'Текст не соответствует выводу (сообщение о выводе не появилось)'


    @allure.title('test invalid_number_of_characters')
    @pytest.mark.negative
    @pytest.mark.parametrize('invalid_number_of_character', ['1', GenerateText.generate_char(26)])
    def test_invalid_number_of_characters(self,page, invalid_number_of_character):
        """
        Тест вводит данные размером в один символ и больше 25, задача - получить ошибку от сайта
        """
        with allure.step(f'Отчищаю поле ввода и ввожу свои данные [{invalid_number_of_character}]'):
            page.clear_text_line()
            page.text_line_set_text(invalid_number_of_character)
        with allure.step(f'Нажимаю ENTER'):
            page.press_enter_in_line()
        with allure.step('Ожидаю сообщение об ошибке'):
            try:
                assert (page.get_error_message_text() == 'Please enter 2 or more characters' or
                        page.get_error_message_text() == 'Please enter no more than 25 characters')
            except TimeoutException:
                page.take_a_screenshot_in_allure(name='fail_screen')
                assert False, 'Текст с ошибкой не отобразился'



    @allure.title('test invalid_characters_in_input')
    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_string", GenerateText.get_invalid_characters())
    def test_invalid_characters_in_input(self,page, invalid_string):
        """
        Тест вводит неверные данные за пользователя, а именно
        запрещенные для этого поля символы (@=+ и др.). Для того чтобы текст прошел условие (не менее 2 символов)
        в строку подставляется слово 'test'
        """
        with allure.step(f'Отчищаю поле ввода и ввожу свои данные [{invalid_string}]'):
            page.clear_text_line()
            page.text_line_set_text(invalid_string)
        with allure.step(f'Нажимаю ENTER'):
            page.press_enter_in_line()

        with allure.step('Ожидаю сообщение об ошибке'):
            try:
                assert page.get_error_message_text() == 'Enter a valid string consisting of letters, numbers, underscores or hyphens.'
            except TimeoutException:
                page.take_a_screenshot_in_allure(name='fail_screen')
                assert False, 'Текст с ошибкой не отобразился'









