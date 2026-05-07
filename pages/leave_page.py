from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LeavePage:
 def __init__(self,driver):
    self.driver=driver


 leave=(By.XPATH,"//span[text()='Leave']")  
 leave_list=(By.XPATH,"//h5[text()='Leave List']")
 leave_status=(By.XPATH,"//label[normalize-space()='Show Leave with Status']/following::div[contains(@class,'oxd-select-text')][1]")
 cancelled_option=(By.XPATH,"//span[normalize-space()='Cancelled']")
 leave_type=(By.XPATH,"//label[text()='Leave Type']/following::*[contains(@class,'oxd-icon bi-caret-down-fill oxd-select-text--arrow')][1]")
 personal_option=(By.XPATH,"//div[normalize-space()='CAN - Personal']")
 employee_name=(By.XPATH,"//input[@placeholder='Type for hints...']")
 sub_unit=(By.XPATH,"//label[normalize-space()='Sub Unit']/following::i")
 engg_option=(By.XPATH,"//div[normalize-space()='Engineering']")
 radio=(By.XPATH,"//p[normalize-space()='Include Past Employees']/following::span[contains(@class,'oxd-switch-input oxd-switch-input--active --label-right')]")
 search_btn=(By.XPATH,"//button[@type='submit']")
 calender=(By.XPATH,"//label[normalize-space()='From Date']/following::input[1]")
 entitlements=(By.XPATH,"//span[normalize-space()='Entitlements']")
 my_entitlements=(By.XPATH,"//a[normalize-space()='My Entitlements']")
 my_leave_text=(By.XPATH,"//h5[normalize-space()='My Leave Entitlements']")

 def click_leave(self):
    self.driver.find_element(*self.leave).click()
    print("hello")
    

 def verify_leave_text(self):
   return self.driver.find_element(*self.leave_list).text
 
 def click_cal(self,cal):
   self.calender.clear()
   self.driver.find_element(*self.calender).send_keys(cal)

 def select_cal(self,cal):
     self.click_cal(cal)
     time.sleep(5)
 
 def select_leave_status(self):
   self.driver.find_element(*self.leave_status).click()

 def select_cancelled(self):
   self.driver.find_element(*self.cancelled_option).click()

 def select_option(self):
  self.select_leave_status()
  self.select_cancelled()
  print("done")
  


 def click_leave_type(self):
   self.driver.find_element(*self.leave_type).click()
   
 def select_personal(self):
   self.driver.find_element(*self.personal_option).click()

 def select_leave_option(self):
  self.click_leave_type()
  self.select_personal()
  print("type")
  
 def enter_username(self,user):
   self.driver.find_element(*self.employee_name).send_keys(user)

 def username_search(self,user):
   self.enter_username(user)
   

 def click_sub_unit(self):
   self.driver.find_element(*self.sub_unit).click()
 def select_engg(self):
   self.driver.find_element(*self.engg_option).click()
 def select_engg_option(self):
   self.click_sub_unit()
   self.select_engg()

 def click_radio(self):
   self.driver.find_element(*self.radio).click()

 def click_search(self):
    self.driver.find_element(*self.search_btn).click()

 def click_leave(self):
    self.driver.find_element(*self.leave).click()
    print("hello")
    time.sleep(2)

 def click_Entitlements(self):
    self.driver.find_element(*self.entitlements).click()

 def select_option_enti(self):
    self.driver.find_element(*self.my_entitlements).click()
 def click_my_entitlements(self):
    self.click_Entitlements()
    self.select_option_enti()

 def verify_my_leave_text(self):
     return self.driver.find_element(*self.my_leave_text).text