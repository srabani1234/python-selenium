from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager

option = webdriver.ChromeOptions()
option.headless=True

browserName = 'chrome'
if browserName.lower() == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
elif browserName.lower() == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Pass correct browser namr:', browserName)
    raise Exception('driver not found')
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/open-source/demo/')
print(driver.title)
ele_industry = driver.find_element(By.ID,'Form_submitRequest_Industry')
ele_country = driver.find_element(By.ID,'Form_submitRequest_Country')
def sel_drop_down(locator,value):
    for ele in locator:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break



country_list = driver.find_elements(By.XPATH,'//select[@id="Form_submitRequest_Country"]/option')
sel_drop_down(country_list,'Iraq')