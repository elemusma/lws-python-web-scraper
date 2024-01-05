import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Get URL
# base_url = "https://latinowebstudio.com/"
base_url = "https://downtoearthinvestments.com/"

# Get contact URL #1
contact_path = "contact/"

# Get contact URL #2
contact_path_two = "contact-us/"

# check HTTP status code using requests library
response = requests.get(base_url)

# print the status code for troubleshooting
print("Status Code:", response.status_code)

# check if response was successful
if response.status_code == 200:
    driver.get(base_url)
    # Pause for 1 seconds
    time.sleep(1)

    driver.get(f"{base_url}{contact_path}")

    # Find the name input field by name attribute
    # name_input = driver.find_element_by_name("name")
    name_input = driver.find_element(By.ID, "input_1_1")
    email_input = driver.find_element(By.ID, "input_1_3")
    message_input = driver.find_element(By.ID, "input_1_4")
    submit_input = driver.find_element(By.ID, "gform_submit_button_1")

    # Clear any existing text in the input field
    name_input.clear()
    email_input.clear()
    message_input.clear()

    # Enter your name
    name_input.send_keys("Python")
    time.sleep(0.5)
    email_input.send_keys("python@gmail.com")
    time.sleep(0.5)
    message_input.send_keys("This is a test of web scraping with Python.")
    time.sleep(0.5)
    submit_input.click()

    time.sleep(1)

# Close the browser window
driver.quit()
