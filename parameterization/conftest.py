from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture(params=["chrome","firefox"],scope="class")
def init_driver(request):
    if request.param == "chrome":
       web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path= GeckoDriverManager().install())
    request.cls.driver = web_driver
    web_driver.get("https://app.hubspot.com/signup-hubspot/crm?loginRedirectUrl=undefined")
    web_driver.implicitly_wait(20)
    yield
    web_driver.close()