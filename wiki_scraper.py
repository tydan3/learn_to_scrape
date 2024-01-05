import requests
from bs4 import BeautifulSoup

# URL of Wikipedia's homepage
url = "https://en.wikipedia.org/wiki/Main_Page"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the "Did You Know" section
    did_you_know_section = soup.find('div', {'id': 'mp-dyk'})

    # Check if "Did You Know" section is found
    if did_you_know_section:
        print("Wikipedia: Did You Know?")
        # Extract and print the titles
        titles = did_you_know_section.find_all('li')
        for title in titles:
            print("Title:", title.get_text())
    else:
        print("Did You Know section not found on the page.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
