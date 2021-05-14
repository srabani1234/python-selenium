from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
act = ActionChains(driver)
driver.find_element(By.NAME,'proceed').click()

alt = driver.switch_to.alert
print(alt.text)
alt.accept()
#alt.dismiss()
# if enter something in alert

#alt.send_keys('Enter something')
driver.switch_to.default_content()

time.sleep(2)
driver.quit()