# Created by jalex at 9/29/2022
Feature: Amazon sign in page
  # Enter feature description here

  Scenario: Verify that logged out user is redirected to 'Sign In' page when clicking on Returns and Orders
    Given open Amazon page
    When Logged out user clicks "Orders and Returns"
    Then User is redirected to Sign in page


