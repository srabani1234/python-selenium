from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName = 'chrome'
if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Pass correct browser namr:' ,browserName)
    raise Exception('driver not found')
driver.get('https://app.hubspot.com/login')
driver.get('https://app.hubspot.com/signup-hubspot/crm?loginRedirectUrl=undefined')
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//a[@data-selenium="login"]').click()
driver.find_element(By.ID,'username').send_keys('srabaniadhikary@yahoo.in')
driver.find_element(By.ID, 'password').send_keys('Oxford@456')
driver.find_element(By.ID, 'loginBtn').click()
print(driver.title)

time.sleep(3)
driver.quit()


