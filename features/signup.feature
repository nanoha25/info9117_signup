# Created by hakur at 7/05/2016
Feature: New user sign up:
  This feature allows new user to add an account into system.

  Scenario: User enter a name which does not exist in database
    When a user enters a name
    And the name does not exist in database
    Then system should allow user to choose this name

  Scenario: User enter a name which does exist in database
    When a user enters a name
    But the name does exist in database
    Then system should tell user this name has been used

  Scenario: User enter a password with only numbers
    When a user set up password
    But the password contains only numbers
    Then system should tell user this password is weak
    And reject this password

  Scenario: User enter a password with letters and numbers
    When a user set up password
    And the password contains numbers and letters
    Then system should tell user this password is good
    And accept this password

  Scenario: User enter a password with only up to 7 characters
    When a user set up password
    But the password is only up to 7 characters long
    Then system should tell user this password is weak
    And reject this password

  Scenario: User enter a valid email address
    When a user set up an email address
    And the email address is a standard email address
    Then system should accept this email address

  Scenario: User enter an invalid email address
    When a user set up an email address
    But the email address is not a standard email address
    Then system should tell user this email is invalid
    And reject this email address

