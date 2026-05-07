Feature: admin functionality

  Background: Valid Login
    Given user is on login page
    When user enters username and password
    And clicks on login button
    When user should be redirected to dashboard

  Scenario:admin module chk
    When user click on admin module
    Then verify the admin text
    When user search a username
    And user assign role
    And user assign status
    Then click on search button