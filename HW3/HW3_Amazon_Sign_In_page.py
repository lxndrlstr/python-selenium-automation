from selenium.webdriver.common.by import By
from behave import given, when, then

@then('User is redirected to Sign in page')
def Sign_in_page(context):
    context.driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').is_displayed()
