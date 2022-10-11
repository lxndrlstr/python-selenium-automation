# Created by jalex at 10/10/2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can add a product to the cart
    Given open Amazon page
    When Search for Jazz Album
    And Click on the first product
    And Click on Add to Cart button
    And Open cart page
    Then Verify Cart has 1 item(s)

