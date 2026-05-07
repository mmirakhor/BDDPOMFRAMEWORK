Feature: Time Module functionality
 Background: Background: Valid Login
    Given user is on login page
    When user enters username and password
    And clicks on login button
    When user should be redirected to dashboard

 Scenario: Verify Employee Timesheets page
  When click on time module
  Then Select Employee text verify
  When enter Employee Name
  And click on view button
  Then verify invalid text

 

 Scenario: verify My Timesheet page
  When user click leave module
  And click on mytimesheets
  And verify submitted text
  Then click on edit button