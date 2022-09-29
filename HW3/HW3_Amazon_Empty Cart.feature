# Created by jalex at 9/29/2022
Feature: Amazon Shopping Cart
  # Enter feature description here

  Scenario: Verifies that Your Amazon Cart is empty
    Given open Amazon page
    When user clicks on cart
    Then cart is empty