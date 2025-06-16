from allure_commons.types import AttachmentType
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,browser):
        self.browser = browser
        """
        При наследовании от этого класса, нужно переопределить аттрибут page_url, который будет хранить в себе
        ссылку на странице с который работаем
        """
        self.page_url = 'https://www.qa-practice.com/'


    def open_page(self):
        """
        Открывает страницу в браузере, url берется из self.page_url
        """
        return self.browser.get(self.page_url)


    def take_a_screenshot_in_allure(self,name='screen',attachment_type=AttachmentType.PNG):
        """
        Метод создает скриншот и автоматически прикрепляет его внутри allure.step внутри которого он был вызван
        """
        allure.attach(self.browser.get_screenshot_as_png(),name=name,attachment_type=attachment_type)


    def find(self,args: tuple[str,str], timeout=0):
        """
        Метод ищет элемент на странице, возвращает WebElement, при передаче параметра timeout, создает ожидание
        на появление элемента на странице
        """
        if timeout:
            self.wait_presence_of_element_located(args,timeout=timeout)
        return self.browser.find_element(*args)


    def wait(self,timeout=10) -> WebDriverWait:
        """
        Создает объект класса WebDriverWait и передает timeout (время ожидания)
        Для использования, обратитесь page.wait(timeout=).until(...)
        """
        wait_driver = WebDriverWait(self.browser,timeout)
        return wait_driver


    def wait_presence_of_element_located(self, selector: tuple[str,str], timeout: int):
        """
        Метод задает время ожидания появления на странице для передаваемого элемента
        """
        return self.wait(timeout).until(EC.presence_of_element_located(selector))

