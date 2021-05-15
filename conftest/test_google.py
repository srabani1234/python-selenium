from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.mark.usefixtures('init_driver')
class Base_Test:
    pass
class Test_Google_Chrome(Base_Test):
    def test_googlr_title_chrome(self):

        assert self.driver.title == "Google"
    def test_googlr_url(self):
        assert self.driver.current_url == 'https://www.google.com/'