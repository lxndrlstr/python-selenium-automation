from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(executable_path=r"C:\Users\jalex\Desktop\QA Auto\python-selenium-automation\chromedriver.exe",options= c)

# open create account page
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=4GGKXZ9X2Q9E9KN3E69G&openid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# verify Amazon Logo is displayed
assert driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo").is_displayed(), 'Logo is not displayed'

# verify "Create Account" text is displayed
assert driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']").is_displayed(), 'Create Account is not displayed'

# verify "Your name" input field is displayed
assert driver.find_element(By.ID,"ap_customer_name").is_displayed(), "'Your name' input field is not displayed"

# verify "Email" input field is displayed
assert driver.find_element(By.ID,"ap_email").is_displayed(), "'Email' input field is not displayed"

# verify "Password" input field is displayed
assert driver.find_element(By.ID,"ap_password").is_displayed(), "'Password' input field is not displayed"

# verify "Re-enter password" input field is displayed
assert driver.find_element(By.ID,"ap_password_check").is_displayed(), "'Re-enter password' input field is not displayed"

# verify "Create your Amazon Account" button is displayed
assert driver.find_element(By.ID,"continue").is_displayed(), "'Continue' button is not displayed"

# verify "Conditions of Use" link is displayed
assert driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']").is_displayed(), "'Conditions of Use' link is not displayed"

# verify "Privacy Notice" link is displayed
assert driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']").is_displayed(), "'Privacy Notice' link is not displayed"

# verify "Sign In" link is displayed
assert driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid']").is_displayed(), "'Sign in' link is not displayed"

driver.quit()
