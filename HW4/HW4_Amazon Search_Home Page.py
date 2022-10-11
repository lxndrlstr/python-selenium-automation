from selenium.webdriver.common.by import By
from behave import given, when, then

@given('open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {product}')
def product_search(context, product):
    element = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    element.send_keys(product)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()
