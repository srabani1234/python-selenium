from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#pass username/password through url to handle browser authentication pop up
driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')