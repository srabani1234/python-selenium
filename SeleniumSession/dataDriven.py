import  xlrd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.orangehrm.com/orangehrm-30-day-trial/')
url_locator = driver.find_element(By.ID,'Form_submitForm_subdomain')
firstname_locator = driver.find_element(By.ID,'Form_submitForm_FirstName')
lastname_locator = driver.find_element(By.ID,'Form_submitForm_LastName')
email_locator = driver.find_element(By.ID,'Form_submitForm_Email')
job_locator = driver.find_element(By.ID,'Form_submitForm_JobTitle')
company_locator = driver.find_element(By.ID,'Form_submitForm_CompanyName')
phone_locator = driver.find_element(By.ID,'Form_submitForm_Contact')
totalemp_locator = driver.find_element(By.ID,'Form_submitForm_NoOfEmployees')
industry_locator = driver.find_element(By.ID,'Form_submitForm_Industry')
country_locator = driver.find_element(By.ID,'Form_submitForm_Country')

workbook = xlrd.open_workbook('data.xlsx')
sheet = workbook.sheet_by_name('login')
rowCount = sheet.nrows
colCount = sheet.ncols
print('row:',+rowCount)
print('col:',+colCount)

for cur_row in range (1,rowCount):
    print(cur_row)
    url_data = sheet.cell_value(cur_row,0)
    firstNane = sheet.cell_value(cur_row,1)
    lastName = sheet.cell_value(cur_row,2)
    emailID = sheet.cell_value(cur_row,3)
    job = sheet.cell_value(cur_row,4)
    company = sheet.cell_value(cur_row,5)
    phone = int(sheet.cell_value(cur_row,6))
    total_emp = sheet.cell_value(cur_row,7)
    industry = sheet.cell_value(cur_row,8)
    country = sheet.cell_value(cur_row,9)
    print(total_emp)

    url_locator.clear()
    url_locator.send_keys(url_data)
    firstname_locator.clear()
    firstname_locator.send_keys(firstNane)
    lastname_locator.clear()
    lastname_locator.send_keys(lastName)
    email_locator.clear()
    email_locator.send_keys(emailID)
    job_locator.clear()
    job_locator.send_keys(job)
    company_locator.clear()
    company_locator.send_keys(company)
    phone_locator.clear()
    phone_locator.send_keys(phone)

    totalemp_locator.send_keys(total_emp)

    industry_locator.send_keys(industry)

    country_locator.send_keys(country)


    time.sleep(10)


driver.quit()