from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(executable_path=r"C:\Users\jalex\Desktop\QA Auto\python-selenium-automation\chromedriver.exe",options= c)

# open Amazon Sign in page
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

# locate Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
expected_result = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
actual_result = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Amazon Logo Test Case Passed')

# locate email field
driver.find_element(By.ID, 'ap_email').send_keys('Test')
expected_result = driver.find_element(By.ID, 'ap_email')
actual_result = driver.find_element(By.ID, 'ap_email')
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Email Field Test Case Passed')

# locate continue button
driver.find_element(By.ID, 'continue')
expected_result = driver.find_element(By.ID, 'continue')
actual_result = driver.find_element(By.ID, 'continue')
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Continue Button Test Case Passed')

# locate need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
expected_result = 'Need help?'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']" ).text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Need Help Link Test Case Passed')

# locate forgot your password link
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-expand']").click()
driver.find_element(By.ID, 'auth-fpp-link-bottom')
expected_result = 'Forgot your password?'
actual_result = driver.find_element(By.ID, 'auth-fpp-link-bottom').text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Forgot Password Test Case Passed')

# locate other issues with sign in link
driver.find_element(By.ID, "ap-other-signin-issues-link")
expected_result = 'Other issues with Sign-In'
actual_result = driver.find_element(By.ID,"ap-other-signin-issues-link").text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Other Issues Test Case Passed')

# locate create your amazon account link
driver.find_element(By.ID, 'createAccountSubmit')
expected_result = 'Create your Amazon account'
actual_result = driver.find_element(By.ID, 'createAccountSubmit').text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Create your Account Test Case Passed')

# locate conditions of use link
driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088"]')
expected_result = 'Conditions of Use'
actual_result = driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088"]').text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Conditions of Use Test Case Passed')

# locate Privacy notice link
driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496"]')
expected_result = 'Privacy Notice'
actual_result = driver.find_element(By.XPATH, '//a[@href="/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496"]').text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Privacy Notice Test Case Passed')

#Test Case: Logged out user sees Sign in page when clicking Orders
driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, '//a[@href="/gp/css/order-history?ref_=nav_orders_first"]').click()
driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]')
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
print('Test Case Passed, Logged out user sees Sign in page when clicking Orders')



driver.quit()


