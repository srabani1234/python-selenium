from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import time

#request.cls is the test class using the fixture, so request.cls.driver = ... is essentially the same as MyTestClass.driver =
# ... if MyTestClass uses the fixture.
@pytest.fixture(scope='class')
def init_chrome_driver(request):
# help of request we can access scope
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver # assign webdriver to class level

    yield
    ch_driver.close()

@pytest.fixture(scope='class')
def init_firefox_driver(request):

    ff_driver = webdriver.firefox(executable_path = GeckoDriverManager().install())
    request.cls.driver =ff_driver
    ff_driver.implictly_wailt(10)

    yield
    ff_driver.close()


@pytest.mark.usefixtures('init_chrome_driver')
class base_Chrome_Test:
    pass
class Test_Google_Chrome(base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
        print('tes+',self.__dict__)


@pytest.mark.usefixtures('init_firefox_driver')
class base_firefox_Test:
    pass
class Test_Google_Firefox(base_firefox_Test):
    def test_google_title_firefox(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"






