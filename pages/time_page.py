from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TimePage:
    def __init__(self,driver):
        self.driver=driver

    time =(By.XPATH,"//span[text()='Time']")
    Select_Employee_text =(By.XPATH,"//h6[normalize-space()='Select Employee']")
    Employee_Name=(By.XPATH,"//label[normalize-space()='Employee Name']/following::input[1]")
    search_btn=(By.XPATH,"//button[@type='submit']")
    invalid=(By.XPATH,"//span[text()='Invalid']")
    timesheets_dropdown = (By.XPATH, "//span[normalize-space()='Timesheets']")
    my_timesheets_option = (By.XPATH, "//a[contains(@class,'oxd-topbar-body-nav-tab-link') and normalize-space()='My Timesheets']")
    
    my_timesheet_text=(By.XPATH,"//p[normalize-space()='Status: Not Submitted']")
    edit_btn=(By.XPATH,"//button[@type='button' and normalize-space()='Edit']")

    

    def click_time(self):
        self.driver.find_element(*self.time).click()
           

    def Select_Employee_verify(self):
        return self.driver.find_element(*self.Select_Employee_text).text

    def enter_employee(self,user):
        self.driver.find_element(*self.Employee_Name).send_keys(user)

    def employee_search(self,user):
        self.enter_employee(user)

    def click_btn(self):
       self.driver.find_element(*self.search_btn).click()

    def select_invalid(self):
        return self.driver.find_element(*self.invalid).text
    
    def click_time(self):
        self.driver.find_element(*self.time).click()
    
    def select_time_sheet_dropdown(self):
        self.driver.find_element(*self.timesheets_dropdown).click()

    def select_my_timesheet(self):
        self.driver.find_element(*self.my_timesheets_option).click()
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(
        # EC.element_to_be_clickable(self.my_timesheets_option)
        # )
        # element.click()

    def select_my_timesheets(self):
        self.select_time_sheet_dropdown()
        self.select_my_timesheet()
        # wait = WebDriverWait(self.driver, 10)

        #  # open dropdown
        # wait.until(EC.element_to_be_clickable(self.timesheets_dropdown)).click()

        #  # click My Timesheets
        # wait.until(EC.element_to_be_clickable(self.my_timesheets_option)).click()


    def my_timesheet_verify(self):
        

        return self.driver.find_element(*self.my_timesheet_text).text
        #  wait = WebDriverWait(self.driver, 20)
        #  element = wait.until(
        # EC.visibility_of_element_located(self.my_timesheet_text)
        # )
        #  return element.text
    
    def click_edit(self):
        self.driver.find_element(*self.edit_btn).click()

    