from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Set up the WebDriver
driver = webdriver.Chrome(service=Service("E:/chromedriver-win64/chromedriver.exe"))

# Open the Hirist website
driver.get('https://hirist.tech')

# Click on 'Jobseeker Login'
jobseeker_login_button = driver.find_element(By.LINK_TEXT, 'Jobseeker Login')
jobseeker_login_button.click()

# Wait for login page to load
time.sleep(2)

# Click on 'Sign in'
sign_in_button = driver.find_element(By.XPATH, "//span[text()='Sign In']")
sign_in_button.click()

# Wait for sign-in form to load
time.sleep(2)

# Enter Email Address
email_field = driver.find_element(By.XPATH, '//input[@placeholder="Enter your registered email id"]')
email_field.send_keys('mayurjadhav1998.mj@gmail.com')

# Enter Password
password_field = driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]')
password_field.send_keys('Mayur@2812')

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the main page to load after login
time.sleep(5)

# Click on 'Frontend Developer' link
try:
    Frontend_developer_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/c/Frontend-developer-jobs.html') and contains(@class, 'dynamic-categories')]"))
    )
    Frontend_developer_link.click()
    print("Navigated to Frontend Developer jobs.")
    time.sleep(3)  # Allow time for the page to load
except TimeoutException:
    print("Failed to navigate to Frontend Developer jobs.")

# Tap on 'Any Exp. Level' dropdown and select '0 - 1 yrs'
try:
    # Locate and click the parent div to open the dropdown
    dropdown_parent = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-jlyJG eMQnym']"))
    )
    dropdown_parent.click()
    time.sleep(1)  # Allow the options to appear

    # Locate and click the '0 - 1 yrs' option
    zero_one_year_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@value='0 - 1 yrs']"))
    )
    zero_one_year_option.click()
    print("Experience level '0 - 1 yrs' selected.")
except TimeoutException:
    print("Failed to select experience level '0 - 1 yrs'.")

# Click the 'Apply' button
try:
    apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@value='Filter' and text()='Apply']"))
    )
    apply_button.click()
    print("Filters applied successfully.")
    time.sleep(5)  # Wait for the page to reload or update filters
except TimeoutException:
    print("Failed to click the 'Apply' button.")

# Select up to 50 items and click 'Apply All'
items = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
for index, item in enumerate(items):
    if index < 50:
        driver.execute_script("arguments[0].scrollIntoView();", item)  # Scroll into view
        driver.execute_script("arguments[0].click();", item)  # Click via JavaScript

# Wait for the 'Apply All' button to become clickable or visible, then click it
try:
    apply_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply All']"))
    )
    driver.execute_script("arguments[0].click();", apply_button)
except TimeoutException:
    print("The 'Apply All' button was not found or clickable within the wait time.")

# Close the WebDriver
time.sleep(2)
driver.quit()
