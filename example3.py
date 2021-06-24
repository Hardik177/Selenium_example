from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import Select
print("sample test case started")  
driver = webdriver.Chrome(executable_path='C:\Chrome\chromedriver')  
driver.maximize_window()  
driver.get("https://katalon-demo-cura.herokuapp.com/")  
 
time.sleep(3)  
  
driver.find_element_by_id("btn-make-appointment").click()
time.sleep(3)  
username=driver.find_element_by_xpath('//*[@id="txt-username"]')
username.send_keys('John Doe')
password=driver.find_element_by_xpath('//*[@id="txt-password"]')
password.send_keys('ThisIsNotAPassword')
driver.find_element_by_id("btn-login").click()
select = Select(driver.find_element_by_id('combo_facility'))
time.sleep(3)
select.select_by_value('Hongkong CURA Healthcare Center')
time.sleep(3)
driver.find_element_by_id("radio_program_medicaid").click()
date=driver.find_element_by_xpath('//*[@id="txt_visit_date"]')
date.send_keys("26/06/2021")
driver.find_element_by_xpath('//*[@id="txt_comment"]').click()
comment=driver.find_element_by_xpath('//*[@id="txt_comment"]')
comment.send_keys("Any Comment")
time.sleep(3)
driver.find_element_by_id("btn-book-appointment").click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="summary"]/div/div/div[7]/p/a').click()
time.sleep(3)
#close the browser  
driver.close()  
print("sample test case successfully completed")  