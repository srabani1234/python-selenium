#Fixtures are functions, which will run before each test function to which it is applied.
# Fixtures are used to feed some data to the tests such as database connections, URLs to test
# and some sort of input data. ...
# Pytest while the test is getting executed, will see the fixture name as input parameter.
#Why Use pytest Fixtures? pytest fixtures are used in python instead of classic xUnit style setup and teardown
# methods where a particular section of code is executed for each test case.

# excat same method name have to use def setup_module(module)/def teardown_module(module)

#to run this test use pytest -v -s classname.py [-v = varbose -s= pring console]
# to generate html report run use: pytest test_fistures.py -v -s --html==test_fistures_report.html
# to get error details in report run: pytest test_fistures.py -v --html=report.html

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

driver =None # use driver as global varable
def setup_module(module):
    global driver

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com/')

def teardown_module(module):
    driver.quit()



def test_google_title():
    assert driver.title == "Google"

def test_google_url():
    assert driver.current_url == "https://www.google.com/h"
