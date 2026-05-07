Feature: Login functionality

  Scenario: Valid Login
    Given user is on login page
    When user enters username and password
    And clicks on login button
    When user should be redirected to dashboard

  Scenario: Invalid Login
    Given user is on login page
    When user enters invalid credentials
    And clicks on login button
    When error message should be displayed