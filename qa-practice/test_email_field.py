import allure
from selenium.common import TimeoutException
from conftest import email_field_page as page
from servises.generate_text import GenerateText
import pytest



class TestEmailFiledPage:
    """
    Здесь тестируется вкладка Email Filed
    """
    @allure.title('test is_displayed')
    def test_line_is_displayed(self, page):
        """
        Тест проверяет отображение поля ввода email для пользователя
        """
        with allure.step('Проверяю отображение поля для ввода email'):
            page.take_a_screenshot_in_allure(name='page_screen')
            assert page.email_input_line_is_displayed()


    @allure.title('test is_enabled')
    def test_line_is_enabled(self,page):
        """
        Тест проверяет доступность поля ввода email для пользователя
        """
        with allure.step('Проверяю доступность поля email ввода для пользователя'):
            assert page.email_input_line_is_enabled()


    @allure.title('test send_email')
    def test_send_email(self,page, email='testemail@localhost.ru'):
        """
        Тест вводит email за пользователя, который соответствует требованиям
        """
        with allure.step(f'Отчищаю поле ввода и ввожу свой email [{email}]'):
            page.clear_text_line().email_input_line_set_text(email)
        with allure.step(f'Нажимаю ENTER'):
            page.press_enter_in_line()
        with allure.step('Ожидаю окошко с результатом ввода, проверяю соответствие'):
            try:
                assert page.get_result_text() == email
            except TimeoutException:
                assert False, 'Текст не соответствует выводу (сообщение о выводе не появилось)'


    @pytest.mark.negative
    @pytest.mark.parametrize('invalid_email', GenerateText.get_invalid_email())
    def test_send_invalid_email(self,page,invalid_email):
        """
        Тест вводит невалидный email в поле и проверят, что сайт его не пропускает
        """
        with allure.step('Очищаю поле для ввода и ввожу неверный email'):
            page.clear_text_line().email_input_line_set_text(invalid_email)
        with allure.step(f'Нажимаю ENTER'):
            page.press_enter_in_line()
        with allure.step('Ожидаю ошибку `Enter a valid email address.`'):
            try:
                assert page.get_error_message_text() == 'Enter a valid email address.'

            except TimeoutException:
                page.take_a_screenshot_in_allure(name='fail_screen')
                assert False, 'Ошибка не появилась на экране'
