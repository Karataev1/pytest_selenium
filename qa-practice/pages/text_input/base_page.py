from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,browser, wait):
        self.browser = browser
        self.wait = wait

    def find(self,args: tuple):
        return self.browser.find_element(*args)