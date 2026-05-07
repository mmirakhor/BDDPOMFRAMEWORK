from behave import *
from pages.time_page import TimePage
import time

@when('click on time module')
def step_impl(context):
    context.time_page =TimePage(context.driver)
    context.time_page.click_time()

@then('Select Employee text verify')
def step_impl(context):
    context.time_page.Select_Employee_verify()

@when('enter Employee Name')
def step_impl(context):
    context.time_page.enter_employee("Mukesh")

@when('click on view button')
def step_impl(context):
    context.time_page.click_btn()

@then('verify invalid text')
def step_impl(context):
    text = context.time_page.select_invalid()
    assert "Invalid" in text
time.sleep(10)

@when('user clicks on Time module')
def step_impl(context):
    context.time_page =TimePage(context.driver)
    context.time_page.click_time()

@when('click on mytimesheets')
def step_impl(context):
    context.time_page.select_my_timesheets()
    time.sleep(10)
    print("hello")
time.sleep(10)
@when('verify submitted text')
def step_impl(context):
    record = context.time_page.my_timesheet_verify()
    assert "Submitted" in record
    print("found")
    
@then('click on edit button')
def step_impl(context):
    context.time_page.click_edit()