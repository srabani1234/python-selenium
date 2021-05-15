from selenium import webdriver
from  webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("_____________test start___________")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")


    yield
    print("___________ende Test __________________")
    driver.quit()
@pytest.mark.usefixtures("init_driver")
def test_google_titlle():
    assert driver.title == "Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.com/8"
