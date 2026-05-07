from selenium.webdriver.common.by import By

class AdminPage:
     def __init__(self,driver):
        self.driver=driver

     admin=(By.XPATH,"//span[text()='Admin']")
     admin_text=(By.XPATH,"//h6[normalize-space()='Admin']")
     username=(By.XPATH,"//label[text()='Username']/following::input[1]")
     user_role_dropdown=(By.XPATH,"//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')]")
     admin_option=(By.XPATH,"//div[@role='listbox']//*[text()='Admin']")
     status_dropdown=(By.XPATH,"//label[text()='Status']/following::*[contains(@class,'oxd-select-text-input')]")
     enabled_option=(By.XPATH,"//div[@role='listbox']//*[text()='Enabled']")
     search_btn=(By.XPATH,"//button[@type='submit']")


     def click_admin(self):
         self.driver.find_element(*self.admin).click()
         
     def admin_verify(self):
         return self.driver.find_element(*self.admin_text).text
     
     def enter_username(self,user):
         self.driver.find_element(*self.username).send_keys(user)

     def click_user_role_dropdown(self):
         self.driver.find_element(*self.user_role_dropdown).click()

     def select_admin_role(self):
         self.driver.find_element(*self.admin_option).click()

     def select_user_role(self):
         self.click_user_role_dropdown()
         self.select_admin_role()

     def select_status_dropdown(self):
         self.driver.find_element(*self.status_dropdown).click()

     def select_enable_option(self):
         self.driver.find_element(*self.enabled_option).click()


     def select_status(self):
         self.select_status_dropdown()
         self.select_enable_option()

     def click_search_button(self):
         self.driver.find_element(*self.search_btn).click()

     def username_search(self,user):
        self.enter_username(user)
        


     