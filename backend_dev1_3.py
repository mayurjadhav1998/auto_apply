from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Set up the WebDriver and maximize the window
driver = webdriver.Chrome(service=Service("E:/chromedriver-win64/chromedriver.exe"))
driver.maximize_window()  # Maximizing the window to ensure visibility of elements

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

# Maximize the window to ensure visibility
driver.maximize_window()

# Click on 'Backend Developer' link
try:
    backend_developer_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/c/backend-developer-jobs.html') and contains(@class, 'dynamic-categories')]"))
    )
    backend_developer_link.click()
    print("Navigated to Backend Developer jobs.")
    time.sleep(3)  # Allow time for the page to load
except TimeoutException:
    print("Failed to navigate to Backend Developer jobs.")

# Tap on 'Any Exp. Level' dropdown and select '1 - 3 yrs'
try:
    dropdown_parent = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-jlyJG eMQnym']"))
    )
    dropdown_parent.click()
    time.sleep(1)

    zero_one_year_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@value='1 - 3 yrs']"))
    )
    zero_one_year_option.click()
    print("Experience level '1 - 3 yrs' selected.")
except TimeoutException:
    print("Failed to select experience level '1 - 3 yrs'.")

# Click the 'Apply' button
try:
    apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@value='Filter' and text()='Apply']"))
    )
    apply_button.click()
    print("Filters applied successfully.")
    time.sleep(5)  # Wait for the page to reload or update filters

    # Scroll down 15 times with an interval of 2 seconds
    for _ in range(15):
        driver.execute_script("window.scrollBy(0, window.innerHeight);")  # Scroll down by one viewport height
        print("Scrolled down.")
        time.sleep(2)
except TimeoutException:
    print("Failed to click the 'Apply' button.")

# Select up to 50 items and click 'Apply All'
items = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
for index, item in enumerate(items):
    if index < 100:
        driver.execute_script("arguments[0].scrollIntoView();", item)
        driver.execute_script("arguments[0].click();", item)

try:
    apply_all_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply All']"))
    )
    driver.execute_script("arguments[0].click();", apply_all_button)
except TimeoutException:
    print("The 'Apply All' button was not found or clickable within the wait time.")

# Close the WebDriver
time.sleep(2)
driver.quit()
