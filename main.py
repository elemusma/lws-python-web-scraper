import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def fill_contact_form(base_url, contact_path, name_value, email_value, message_value):
    driver = webdriver.Chrome()

    try:
        # Check HTTP status code using requests library
        response = requests.get(base_url)

        # Print the status code for troubleshooting
        print("Status Code:", response.status_code)

        # Check if the response was successful
        if response.status_code == 200:
            driver.get(base_url)
            # Pause for 1 second
            time.sleep(1)

            driver.get(f"{base_url}{contact_path}")

            # Find the input fields by ID
            label_text = "Name"
            print("label_text success")
            label_element = driver.find_element(By.XPATH, f'//*[text()="{label_text}"]')
            print("label_element success")
            name_input = label_element.find_element(
                By.XPATH, "./following-sibling::div//input"
            )
            print("name_input success")

            # name_input = driver.find_element(By.ID, "input_1_1")
            email_input = driver.find_element(By.ID, "input_1_3")
            message_input = driver.find_element(By.ID, "input_1_4")
            submit_input = driver.find_element(By.ID, "gform_submit_button_1")

            # Clear any existing text in the input fields
            name_input.clear()
            email_input.clear()
            message_input.clear()

            # Enter values into the input fields
            name_input.send_keys(name_value)
            time.sleep(0.5)
            email_input.send_keys(email_value)
            time.sleep(0.5)
            message_input.send_keys(message_value)
            time.sleep(0.5)

            # Submit the form
            submit_input.click()

            time.sleep(1)

    finally:
        # Close the browser window, regardless of success or failure
        driver.quit()


# Example usage
base_url = "https://latinowebstudio.com/"
contact_path = "contact/"
fill_contact_form(
    base_url,
    contact_path,
    "Python",
    "python@gmail.com",
    "This is a test of web scraping with Python. with function.",
)
