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
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')
driver.find_element(By.ID,'justAnInputBox').click()
def select_value_dropdown(locator,value_list):
  if not value_list[0] == 'All':
    for ele in locator:
        print(ele.text)
        for k in range (len(value_list)):

            if ele.text == value_list[k]:
                print('/k no:',k)
                print('k print:', value_list[k])
                ele.click()
                break
  else:
      try:
        for ele in (locator):
          ele.click()
      except Exception as e:
          print(e)



dropdownListLocator = driver.find_elements(By.XPATH,'//span[@class="comboTreeItemTitle"]')
# select multiple value
#value_list = ['choice 6','choice 6 2 2','choice 7']
#value_list =['choice 6']
# select all value
value_list = ['All']
select_value_dropdown(dropdownListLocator,value_list)
driver.quit()


