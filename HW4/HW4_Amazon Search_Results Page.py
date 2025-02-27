from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

@when ('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()

