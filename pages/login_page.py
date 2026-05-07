# from selenium.webdriver.common.by import By

# class LoginPage:
#     def __init__(self,driver):
#         self.driver=driver
#         self.username_field=(By.NAME,"username")
#         self.password_field=(By.NAME,"password")
#         self.login_button=(By.XPATH,"//button[@type='submit']")
#         self.invalid_creads=(By.XPATH,"//div[@class='oxd-alert-content oxd-alert-content--error']")
        


#     def enter_username(self,username):
#         self.driver.find_element(*self.username_field).send_keys(username)
#     def enter_password(self,password):
#         self.driver.find_element(*self.password_field).send_keys(password)
#     def click_login(self):
#         self.driver.find_element(*self.login_button)

#     def login(self,username,password):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_login()
#######################################################################################

# from selenium.webdriver.common.by import By

# class LoginPage:

#     def __init__(self, driver):
#         self.driver = driver

#     # Locators
#     username = (By.NAME, "username")
#     password = (By.NAME, "password")
#     login_btn = (By.XPATH, '//button[@type="submit"]')
#     error_msg = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")

#     # Actions
#     def enter_username(self, user):
#         self.driver.find_element(*self.username).send_keys(user)

#     def enter_password(self, pwd):
#         self.driver.find_element(*self.password).send_keys(pwd)

#     def click_login(self):
#         self.driver.find_element(*self.login_btn).click()

#     def login(self, user, pwd):
#         self.enter_username(user)
#         self.enter_password(pwd)
#         self.click_login()

#     def get_error_message(self):
#         return self.driver.find_element(*self.error_msg).text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    username = (By.NAME,"username")
    password = (By.NAME,"password")
    login_btn = (By.XPATH,'//button[@type="submit"]')
    dashboard=(By.XPATH,"//h6[normalize-space()='Dashboard']")
    error_msg=(By.XPATH,"//p[contains(@class,'oxd-alert-content-text')]")

    def enter_username(self,user):
         self.driver.find_element(*self.username).send_keys(user)

    def enter_password (self,pwd):
         self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
         self.driver.find_element(*self.login_btn).click()

    def login(self,user,pwd):
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_login()

    def verify_dashboard(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
        EC.visibility_of_element_located(self.dashboard)
        )
        return element.text
    
    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
