from behave import given, when, then
# Ye 3 keywords import kiye
# Taaki tu @given, @when, @then likh sake

from pages.login_page import LoginPage
# login_page.py file se LoginPage class le raha hai
# Ye class browser pe kaam karegi (username, password fill etc.)


@given('user is on login page')

def step_impl(context):
    # Ye function hai jo run hoga

    # context = ek box hai jisme data store hota hai (shared memory)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Browser open karega (driver already bana hua hai)
    # Is URL pe le jayega (login page open)
    context.login_page = LoginPage(context.driver)
    # LoginPage ka object bana
    # Driver pass kiya
    # Isko context.login_page me store kiya
    # context.<page_name> = <PageClass>(driver)
    # car = Car()
    # LoginPage = ek class hai (POM file se)
    #context.driver = browser driver
    


@when('user enters username and password')
def step_impl(context):
    context.login_page.login("Admin", "admin123")
    # "Admin" = username (tu manually de raha)
    # "admin123" = password


@when('user enters invalid credentials')
def step_impl(context):
    context.login_page.login("Admin", "wrongpass")


@when('clicks on login button')
def step_impl(context):
    # already handled inside login()
    pass


@when('user should be redirected to dashboard')
def step_impl(context):
    dash=context.login_page.verify_dashboard()
    assert "Dashboard" in dash
    # Current URL check karega
    # Agar "dashboard" hai → PASS
    # Nahi hai → FAIL 

    # 👉 Ye check kar raha:

    # “Current URL me ‘dashboard’ word hai kya?”

    # 🧠 Breakdown
    # 🔹 context.driver.current_url

    # 👉 Browser ka current URL deta hai

    # Example:

    # https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index
    # 🔹 .lower()

    # 👉 Sab letters small bana deta hai
     #element = context.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
     # assert element.is_displayed()



     


@when('error message should be displayed')
def step_impl(context):
    error = context.login_page.get_error_message()
    assert "Invalid credentials" in error