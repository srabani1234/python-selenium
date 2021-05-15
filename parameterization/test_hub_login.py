from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pytest

@pytest.mark.usefixtures('init_driver')
class Base_Test:
    pass
class Test_Hub_Login(Base_Test):
    @pytest.mark.parametrize(
         "username, password",
          [('srabaniadhikary@yahoo.in','Oxford@456'),
             ('srab','Srabani')]

    )
    def test_login(self,username,password):
        self.driver.find_element(By.LINK_TEXT,'Sign in').click()
        self.driver.find_element(By.ID,'username').send_keys(username)
        self.driver.find_element(By.ID,'password').send_keys(password)
        self.driver.find_element(By.ID,'loginBtn').click()