# Created by hakur at 8/05/2016
Feature: A form for guests to contact company
  This is a form which anyone can send feedback to the company.
  Sending feedback does not need user to register an account.
  User should not be asked to register account after sending feedback.

  Scenario: Empty title in contact form
    When user fill contact form
    But title is empty
    Then system should notify user to enter a title of this feedback
    And prevent user from submitting

  Scenario: Empty contents in contact form
    When user fill contact form
    But enquiry area is empty
    Then system should notify user to enter detailed info about this feedback
    And prevent user from submitting

  Scenario: Empty email address in contact form
    When user fill contact form
    And does not fill email address
    Then system should tell user company cannot contact user about this feedback
    But allow user to submit

  Scenario: Invalid email address in contact form
    When user fill contact form
    But fill an invalid email address
    Then system should tell user email address is invalid
    And prevent user from submitting

# do we need to specify "a normal submission" as a separate scenario?