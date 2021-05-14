from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://www.londonfreelance.org/courses/frames/index.html')
act = ActionChains(driver)
time.sleep(10)
frame_ele = driver.find_element(By.NAME,'content')
driver.switch_to.frame(frame_ele)
text_ele =driver.find_element(By.CSS_SELECTOR,'body h1')
print(text_ele.text)
driver.switch_to.parent_frame()
driver.switch_to.default_content()