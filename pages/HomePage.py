from pages.BasePage import TestBasePage
from selenium import webdriver
from selenium.webdriver.common.by import By




class HomePgae(TestBasePage):
    HEADER=(By.XPATH,"//div[@class='private-header__title private-page__title']/h1")
    SETTINGS_ICON =(By.XPATH,'//a[@id="F"]')
    ACCOUNT_DEFAULT = (By.XPATH,'//a[@data-selenium-id="Account Defaults"]')
    ACCOUNT_NAME = (By.XPATH,'//input[@data-test-id="account-name-editor"]')
    SAVE_BUTTON = (By.XPATH,'//button[@data-test-id="save-footer-confirm-btn"]')

    def __init__(self,driver):
        super().__init__(driver)

    def get_Home_Page_Title(self):
        title = self.get_title()
        return title
    def is_setting_icon_exist(self):
        element=self.is_enable(self.SETTINGS_ICON)
        return element
    def get_Header_Value(self):
        self.is_enable(self.HEADER)
        return self.get_ele_Text(self.HEADER)
    def update_account_details(self,accountname):
        self.do_click(self.SETTINGS_ICON)
        self.do_click(self.ACCOUNT_DEFAULT)
        self.do_send_keys(self.ACCOUNT_NAME,accountname)
        self.do_click(self.SAVE_BUTTON)
        return self.get_ele_Text(self.ACCOUNT_NAME)
