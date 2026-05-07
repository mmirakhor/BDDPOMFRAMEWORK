from behave import *
from pages.admin_page import AdminPage



@when('user click on admin module')
def step_impl(context):
        context.admin_page = AdminPage(context.driver)
        
        context.admin_page.click_admin()



@then('verify the admin text')
def step_impl(context):
        text = context.admin_page.admin_verify()
        assert "Admin" in text


@when('user search a username')
def step_impl(context):
        context.admin_page.enter_username("Mukesh")

@when('user assign role')
def step_impl(context):
        context.admin_page.select_user_role()

@when('user assign status')
def step_impl(context):
        context.admin_page.select_status()


@then('click on search button')
def step_impl(context):
       context.admin_page.click_search_button()