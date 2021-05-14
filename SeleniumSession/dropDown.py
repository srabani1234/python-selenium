from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager

browserName = 'chrome'
if browserName.lower() == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName.lower() == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Pass correct browser namr:', browserName)
    raise Exception('driver not found')
driver.implicitly_wait(10)
driver.get('https://www.orangehrm.com/open-source/demo/')
ele_industry = driver.find_element(By.ID,'Form_submitRequest_Industry')
ele_country = driver.find_element(By.ID,'Form_submitRequest_Country')
# select one by one

#seleIndustry = Select(ele_industry)
#seleIndustry.select_by_index(1)
#seleIndustry.select_by_value('Automotive')
#seleIndustry.select_by_visible_text('Computer / Technology - Manufacturer')
#print(seleIndustry.is_multiple)

# commom function for select
#def selectCommonFunction(element,value):
#   selectLocator = Select(ele_industry)
#    selectLocator.select_by_value(value)
#selectCommonFunction(ele_industry,'Automotive')

# get option list using select
#selCountryLocator = Select(ele_country)
#optionList= selCountryLocator.options
#size = len(optionList)
#print(size)
#for ele in  (optionList):
#    print(ele.text)
#    if ele.text == 'Vietnam':
       # selCountryLocator.select_by_value(ele.text)
#       ele.click()
#       break

# get option list element without using select

def select_dropDoen(option_list_locator,value):
    print(len(option_list_locator))
    for ele in (option_list_locator):
        print(ele.text)
        if ele.text == value:

            ele.click()
            break


country_list = driver.find_elements(By.XPATH,'//select[@id="Form_submitRequest_Country"]/option')
driver.implicitly_wait(10)
select_dropDoen(country_list,'Panama')

