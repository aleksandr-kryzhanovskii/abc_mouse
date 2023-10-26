# Created by aleksandrkryzhanovskii at 10/26/23
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Verify sign up
    Given Open ABC Mouse page
    When Click sign up button
    Then Verify https://www.abcmouse.com/abt/register link returned
    When Input testemail@gmail.com into email field
    When Click Submit button
    Then Verify https://www.abcmouse.com/abt/subscription link returned
    Then Verify Become a Member! text is present