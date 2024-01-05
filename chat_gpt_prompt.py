import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Chrome driver
chrome_driver_path = webdriver.Chrome(
    # executable_path="chromedriver-mac-arm64/chromedriver"
    executable_path="/Users/efrainlemus-martinez/Desktop/Latino-Web-Studio/Outscraper/chromedriver-mac-arm64/chromedriver"
)  # Replace with the actual path
print("chrome_driver_path worked")

# Create a dictionary with the Chrome options and set the executable path
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_driver_path
print("chrome_service worked")

# Create a new instance of the Chrome driver with the specified options
driver = webdriver.Chrome(chrome_options=chrome_options)
print("driver worked")

# Base URL
base_url = "https://latinowebstudio.com"

# Define the path for the contact page
contact_path = "/contact/"

# Create the full contact URL
contact_url = base_url + contact_path

# Navigate to the contact page
driver.get(contact_url)

# Check the HTTP status code using requests library
response = requests.get(contact_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(f"Page '{contact_url}' is accessible (status code 200).")

    # # Find the form elements and fill them out
    # name_input = driver.find_element_by_name("name")
    # email_input = driver.find_element_by_name("email")
    # message_input = driver.find_element_by_name("message")

    # name_input.send_keys("Your Name")
    # email_input.send_keys("your@email.com")
    # message_input.send_keys("Your message here")

    # # Submit the form
    # message_input.send_keys(Keys.RETURN)

# Close the browser window
driver.close()
