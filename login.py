from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from datetime import datetime

# Replace with the URL of the login page
login_url = ""
attendance_url = ""

# Replace with your login credentials
username = ""
password = ""

# Prompt for the date range input
datefrom = input("Enter start date (MM/DD/YYYY): ")
dateto = datetime.today().strftime('%m/%d/%Y')  # Current date in MM/DD/YYYY format

# Specify the path to your Chrome WebDriver executable
chrome_driver_path = "{location}/chromedriver-win64/chromedriver.exe"

# Create a ChromeOptions instance and set the executable path
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_driver_path

# Create a new instance of the Chrome web driver with options
driver = webdriver.Chrome(options=chrome_options)

# Open the login page
driver.get(login_url)

#time.sleep(2)

wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.visibility_of_element_located((By.ID, "TxtloginID")))

password_field = driver.find_element(By.ID, "TxtPwd")  # Replace with the actual ID

username_field.send_keys(username)

password_field.send_keys(password)

# Submit the form
password_field.send_keys(Keys.RETURN)

# Open the login page
driver.get(attendance_url)

# Wait for element to load
wait = WebDriverWait(driver, 10)
date_from = wait.until(EC.visibility_of_element_located((By.ID, "ContentPlaceHolder1_TxtDateFrom")))

# Wait for element to load
wait = WebDriverWait(driver, 10)
date_from = wait.until(EC.visibility_of_element_located((By.ID, "ContentPlaceHolder1_TxtDateFrom")))

date_to = driver.find_element(By.ID, "ContentPlaceHolder1_TxtDateTo")
dropdown = Select(driver.find_element(By.ID, "ContentPlaceHolder1_DDLDepartment"))

#Input date
date_from.send_keys(datefrom)
date_to.send_keys(dateto)

# Select dropdown
dropdown.select_by_value("1017")

# Search button
button = driver.find_element(By.ID, "ContentPlaceHolder1_Button1")
button.click()

# Wait for user input before ending the script
input("Press Enter to exit...")

# Close the browser
driver.quit()
