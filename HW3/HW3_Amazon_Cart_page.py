from selenium.webdriver.common.by import By
from behave import given, when, then

@then ('cart is empty')
def empty_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[class*='empty']")