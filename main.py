import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def finding_name_field():
    exit


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

            ########################################################################
            # Start of finding name field

            label_text_first = "First Name"
            label_text_full = "Full Name"
            label_text = "Name"
            print("label_text success")

            try:
                label_element = driver.find_element(
                    By.XPATH, f'//*[text()="{label_text_first}"]'
                )
            except NoSuchElementException:
                try:
                    label_element = driver.find_element(
                        By.XPATH, f'//*[text()="{label_text_full}"]'
                    )
                except NoSuchElementException:
                    try:
                        label_element = driver.find_element(
                            By.XPATH, f'//*[text()="{label_text}"]'
                        )
                    except NoSuchElementException:
                        print(
                            f"All three variations of label text '{label_text_first}' and '{label_text}' not found."
                        )
            # Handle the case when both variations are not found

            print("label_element success")

            name_input = label_element.find_element(
                By.XPATH, "./following-sibling::div//input"
            )
            print("name_input success")

            ########################################################################

            ########################################################################
            # Start of finding email field

            # label_email_first = "Email Address"
            # label_email_full = "Enter Email"
            label_email = "Email"
            print("label_email success")

            email_element = driver.find_element(
                By.XPATH, f'//*[text()="{label_email}"]'
            )

            # try:
            #     email_element = driver.find_element(
            #         By.XPATH, f'//*[text()="{label_email_first}"]'
            #     )
            # except NoSuchElementException:
            #     try:
            #         email_element = driver.find_element(
            #             By.XPATH, f'//*[text()="{label_email_full}"]'
            #         )
            #     except NoSuchElementException:
            #         try:
            #             email_element = driver.find_element(
            #                 By.XPATH, f'//*[text()="{label_email}"]'
            #             )
            #         except NoSuchElementException:
            #             print(
            #                 f"All three variations of label text '{label_email_first}', '{label_email_full}', and '{label_email}' not found."
            #             )
            #             return  # Add a return statement to exit the function if the email field is not found

            # Handle the case when both variations are not found
            # print("email_element success")

            email_input = email_element.find_element(
                By.XPATH, "./following-sibling::div//input"
            )
            print(f"{email_input} success")

            ########################################################################

            # name_input = driver.find_element(By.ID, "input_1_1")
            # email_input = driver.find_element(By.ID, "input_1_3")
            message_input = driver.find_element(By.ID, "input_1_4")
            submit_input = driver.find_element(By.ID, "gform_submit_button_1")

            # Clear any existing text in the input fields
            name_input.clear()
            print("name_input clear")
            email_input.clear()
            print("email_input clear")
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
    "This is a test of web scraping with Python. with function. email element input",
)
