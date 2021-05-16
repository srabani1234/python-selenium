from selenium import webdriver

from config.config import TestData
from pages.BasePage import TestBasePage
from  selenium.webdriver.common.by import By

from pages.HomePage import HomePgae


class LoginPage(TestBasePage):
    SIGN_BTN = (By.LINK_TEXT,'Sign in')
    EMAIL = (By.ID,'username')
    PASSWORD = (By.ID,'password')
    LOGIN = (By.ID,'loginBtn')
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self):
       return self.get_title()

    def is_signup_link_exist(self):
        return self.is_enable(LoginPage.SIGN_BTN)

    def do_Login(self,username,password):
        self.do_click(self.SIGN_BTN)
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN)
        return HomePgae(self.driver)


