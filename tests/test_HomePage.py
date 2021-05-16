from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest
import pytest


class Test_HomePage(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage=self.loginPage.do_Login(TestData.USER_NAME,TestData.USER_PASSWORD)
        home_title=self.homePage.get_Home_Page_Title()
        assert home_title == TestData.HOME_TITLE

    def test_present_setting_icon(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_Login(TestData.USER_NAME, TestData.USER_PASSWORD)
        assert self.homePage.is_setting_icon_exist()
    def test_verify_header_value(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_Login(TestData.USER_NAME, TestData.USER_PASSWORD)
        header_value=self.homePage.get_Header_Value()
        assert header_value == TestData.HOME_HEADER
    def test_account_default(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_Login(TestData.USER_NAME, TestData.USER_PASSWORD)
        account_name= self.homePage.update_account_details(TestData.ACCOUNT_NAME)
        assert account_name == TestData.ACCOUNT_NAME



