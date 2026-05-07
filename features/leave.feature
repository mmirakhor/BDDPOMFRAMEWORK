Feature: Time Module functionality
 Background: Background: Valid Login
    Given user is on login page
    When user enters username and password
    And clicks on login button
    When user should be redirected to dashboard


 Scenario:verify Employee leave page
    When user click on leave module
    Then verify leave list text
    When user enter date
    And user verify leave status
    And enter leave type
    And Employee Name enter
    And select sub unit
    And handle radio button
    Then click on search but


 
 Scenario:verify My Entitlements Module
    When user click on leave module
    And user my Entitlements module
    And verify my leave text
    And user enter leave type
    And user enter leave period
    Then click on search