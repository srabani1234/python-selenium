from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(params =["chrome","firefox"],scope='class')
def init_driver(request):
    if request.param == 'chrome':
       web_driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        web_driver = webdriver.firefox(executable_path = GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures('init_driver')
class Base_Test:
    pass
class Test_Google(Base_Test):
    def test_google_title(self):
        self.driver.get('http://www.google.com')
        assert  self.driver.title == "Google"
    def test_google_url(self):
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"
        #
