import requests
from bs4 import BeautifulSoup

# Replace this URL with the website you want to scrape
# url = "https://latinowebstudio.com"
url = "https://insideoutcreative.io/"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the first h1 element on the page
    h1_element = soup.find("h1")

    # Print the text content of the h1 element
    if h1_element:
        print("H1 Text:", h1_element.text)
    else:
        print("No h1 element found on the page.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
