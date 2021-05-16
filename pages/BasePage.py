from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""This class base class of other class"""

class TestBasePage:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self,ele_locator):
       WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(ele_locator)).click()

    def do_send_keys(self,ele_locator,text):
        #self.driver.find_element(ele_locator).send_keys(text)
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(ele_locator)).clear()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(ele_locator)).send_keys(text)
    def get_ele_Text(self,ele_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(ele_locator))
        return element.text
    def is_enable(self,ele_locator):
        element =WebDriverWait(self.driver,10).until(EC.presence_of_element_located(ele_locator))
        return bool(element)
    def get_title(self):
        #WebDriverWait(self.driver,10).until(EC.title_is(title1))
        return self.driver.title

