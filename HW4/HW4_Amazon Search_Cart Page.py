from selenium.webdriver.common.by import By
from behave import given, when, then

@when ('Open cart page')
def open_cart_page(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then ('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(By.ID, 'nav-cart-count').text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'
