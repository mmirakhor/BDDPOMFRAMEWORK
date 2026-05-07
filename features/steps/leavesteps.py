from behave import *
from pages.leave_page import LeavePage
import time



@when('user click on leave module')
def step_impl(context):
   context.leave_page=LeavePage(context.driver)
   context.leave_page.click_leave()


@then('verify leave list text')
def step_impl(context):
   text=context.leave_page.verify_leave_text()
   assert "Leave List" in text

@when('user enter date')
def step_impl(context):
   context.leave_page.click_cal("2026-05-05")

@when('user verify leave status')
def step_impl(context):
    context.leave_page.select_option()
    

@when('enter leave type')
def step_impl(context):
   context.leave_page.select_leave_option()
print("mukesh")

@when('Employee Name enter')
def step_impl(context):
   context.leave_page.enter_username("Mukesh")
   print("1")


@when('select sub unit')
def step_impl(context):
   context.leave_page.select_engg_option()

@when('handle radio button')
def step_impl(context):
   context.leave_page.click_radio()

@then('click on search but')
def step_impl(context):
   context.leave_page.click_search()

@when('user click leave module')
def step_impl(context):
   context.leave_page=LeavePage(context.driver)
   context.leave_page.click_leave()



@when('user my Entitlements module')
def step_impl(context):
    context.leave_page.click_my_entitlements()

@when('verify my leave text')
def step_impl(context):
   text=context.leave_page.verify_my_leave_text()
   assert "My Leave Entitlements" in text

@when('user enter leave type')
def step_impl(context):
    pass

@when('user enter leave period')
def step_impl(context):
    pass

@then('click on search')
def step_impl(context):
    pass