### Selenium Automation Script for Job Application on Hirist

Author: Mayur Jadhav
Date: 27-10-2024

This script automates the process of logging into the Hirist job portal and applying for job postings by selecting checkboxes for job listings.

### Overview:
1. **Setup WebDriver**: Initializes the Chrome WebDriver and navigates to the Hirist website.
2. **Login**: Automates the login process by clicking on the 'Jobseeker Login' link, entering the email and password, and submitting the login form.
3. **Job Selection**: Finds all job listings on the page, clicks on the checkboxes to select up to 100 job postings, and scrolls the page as necessary to ensure that items are visible before clicking.
4. **Apply All**: Waits for the 'Apply All' button to become clickable and clicks it to submit applications for the selected job postings.
5. **Cleanup**: Closes the browser after a short wait to ensure the user can see the result.

### Dependencies:
- Selenium WebDriver: Ensure you have the `selenium` package installed.
- WebDriver Manager: Used for automatically managing browser drivers.

### Usage:
1. Install required packages:
   ```bash
   pip install selenium webdriver-manager
Ensure ChromeDriver is compatible with your version of Chrome.
Update the script with your registered email and password for the Hirist platform.
2. Run the script using Python:
   ```bash
    python combined_script.py
