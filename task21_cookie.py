from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the website
    driver.get("https://www.saucedemo.com/")
    
    # Get cookies before login
    cookies_before_login = driver.get_cookies()
    print("Cookies before login:")
    for cookie in cookies_before_login:
        print(cookie)

    # Find the username and password fields and log in
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Enter login details
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Wait for a few seconds to ensure the login process completes
    time.sleep(5)

    # Get cookies after login
    cookies_after_login = driver.get_cookies()
    print("\nCookies after login:")
    for cookie in cookies_after_login:
        print(cookie)
    
finally:
    # Close the WebDriver
    driver.quit()

