from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://demo.guru99.com/test/simple_context_menu.html')
right_click_button = driver.find_element(By.CLASS_NAME,'context-menu-one')
act = ActionChains(driver)
act.context_click(right_click_button).perform()
driver.implicitly_wait(20)
right_click_ele = driver.find_elements(By.CSS_SELECTOR,'li.context-menu-item span')
for ele in (right_click_ele):
    print(ele.text)
    if ele.text == 'Paste':
        ele.click()
        break
#driver.quit()

#Action class use for send_key_to_element
userNameEle = driver.find_element(By.ID,'user')
passWordFile = driver.find_element(By.ID,'pass')
act = ActionChains(driver)
act.send_keys_to_element(userNameEle,'value')
act.send_keys_to_element(passWordFile,'value')