from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
act = ActionChains(driver)
source_ele = driver.find_element(By.ID,'draggable')
target_ele = driver.find_element(By.ID,'droppable')
#drirect drag and drop
#act.drag_and_drop(source_ele,target_ele).perform()
# drag hold and dorop
act.click_and_hold(source_ele).move_to_element(target_ele).release().perform()
driver.quit()
