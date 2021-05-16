import pytest

from config.config import TestData
from pages.BasePage import TestBasePage
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest


class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        link= self.loginPage.is_signup_link_exist()
        assert link
    def test_login_Page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title()
        assert title == TestData.LOGIN_TITLE

    def test_login(self):
        self.loginPage =LoginPage(self.driver)
        self.loginPage.do_Login(TestData.USER_NAME,TestData.USER_PASSWORD)
