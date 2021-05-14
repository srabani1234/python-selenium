from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\adhikary_s\\Documents\\driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("Naveen automation labs")
optionlist = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print(len(optionlist))
for ele in range (optionlist):
    print(ele.text)

    if ele.text == 'naveen automation labs github':
        ele.click()
        break


time.sleep(5)
driver.quit()