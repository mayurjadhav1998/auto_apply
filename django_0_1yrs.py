from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time

# Set up the WebDriver
driver = webdriver.Chrome(service=Service("E:/chromedriver-win64/chromedriver.exe"))

# Maximize the browser window
driver.maximize_window()

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

# Hover over 'Backend Developer' and click 'Django'
try:
    backend_developer_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/c/backend-developer-jobs.html')]"))
    )
    # Hover over 'Backend Developer'
    actions = ActionChains(driver)
    actions.move_to_element(backend_developer_link).perform()
    print("Hovered over 'Backend Developer'.")
    time.sleep(2)

    # Click 'Django' link
    django_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/k/django-jobs.html')]"))
    )
    django_link.click()
    print("Navigated to Django jobs.")
    time.sleep(3)  # Allow time for the page to load
except TimeoutException:
    print("Failed to navigate to Django jobs.")

# Tap on 'Any Exp. Level' dropdown and select '0 - 1 yrs'
try:
    dropdown_parent = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-jlyJG eMQnym']"))
    )
    dropdown_parent.click()
    time.sleep(1)

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
try:
    items = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
    for index, item in enumerate(items):
        if index < 50:
            driver.execute_script("arguments[0].scrollIntoView();", item)  # Scroll into view
            driver.execute_script("arguments[0].click();", item)  # Click via JavaScript
    print("Selected up to 50 checkboxes.")

    # Wait for the 'Apply All' button to become clickable
    apply_all_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply All']"))
    )
    driver.execute_script("arguments[0].click();", apply_all_button)
    print("Applied to all jobs.")
except TimeoutException:
    print("The 'Apply All' button was not found or clickable within the wait time.")

# Close the WebDriver
time.sleep(2)
driver.quit()
