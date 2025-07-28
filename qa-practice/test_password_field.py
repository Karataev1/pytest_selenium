import allure
from selenium.common import TimeoutException
from conftest import password_field_page as page
from servises.generate_text import GenerateText
import pytest



class TestPasswordFiledPage:
    """
    Здесь тестируется вкладка Password Filed
    """
    @allure.title('test is_displayed')
    def test_line_is_displayed(self, page):
        """
        Тест проверяет отображение поля ввода password для пользователя
        """
        with allure.step('Проверяю отображение поля для ввода password'):
            page.take_a_screenshot_in_allure(name='page_screen')
            assert page.password_input_line_is_displayed()


    @allure.title('test is_enabled')
    def test_line_is_enabled(self,page):
        """
        Тест проверяет доступность поля ввода password для пользователя
        """
        with allure.step('Проверяю доступность поля password ввода для пользователя'):
            assert page.password_input_line_is_enabled()


    def test_send_valid_password(self,page,password='Aa@1123123'):
        """
        Тест проверяет пропуск валидной строки используемой как password
        """
        with allure.step(f'Отчищаю поле ввода и ввожу свой password [{password}]'):
            page.clear_text_line().password_input_line_set_text(password)
        with allure.step(f'Нажимаю ENTER'):
            page.press_enter_in_line()
        with allure.step('Ожидаю окошко с результатом ввода, проверяю соответствие'):
            try:
                assert page.get_result_text() == password
            except TimeoutException:
                page.take_a_screenshot_in_allure(name='fail_screen')
                assert False, 'Текст не соответствует выводу (сообщение о выводе не появилось)'

    @pytest.mark.negative
    @pytest.mark.parametrize('invalid_password', GenerateText.get_invalid_password())
    def test_send_invalid_password(self,page,invalid_password):
        """
        Тест вводит невалидный invalid_password в поле и проверят, что сайт его не пропускает
        """
        with allure.step('Очищаю поле для ввода и ввожу неверный password'):
            page.clear_text_line().password_input_line_set_text(invalid_password)
        with allure.step(f'Нажимаю ENTER'):
            page.press_enter_in_line()
        with allure.step('Ожидаю ошибку `Low password complexity`'):
            try:
                assert page.get_error_message_text() == 'Low password complexity'
            except TimeoutException:
                page.take_a_screenshot_in_allure(name='fail_screen')
                assert False, 'Ошибка не появилась на экране'