from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
uploadBtn = driver.find_element(By.NAME,'upfile').send_keys('C:\\Users\\adhikary_s\\Pictures\\Camera Roll\\flower.png')