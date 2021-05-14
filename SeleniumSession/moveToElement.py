from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.spicejet.com/')
act = ActionChains(driver)
login_ele = driver.find_element(By.ID,'ctl00_HyperLinkLogin')
act.move_to_element(login_ele).perform()
driver.implicitly_wait(10)
member_login_ele = driver.find_element(By.LINK_TEXT,'SpiceClub Members')
act.move_to_element(member_login_ele).perform()
driver.quit()