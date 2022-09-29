from selenium.webdriver.common.by import By
from behave import given, when, then

@given('open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Logged out user clicks "Orders and Returns"')
def Order_and_Returns(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('user clicks on cart')
def Cart_click(context):
    context.driver.find_element(By.ID, 'nav-cart').click()





