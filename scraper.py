import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request to the website
url = 'https://google.com'
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
  # Step 2: Parse the HTML content of the page
  soup = BeautifulSoup(response.text, 'html.parser')

  # Step 3: Extract information from the parsed HTML
  # Example: Get the title of the page
  title = soup.title.text
  print(f'Title of the page: {title}')
  
  # Example: Get all the links on the page
  # links = soup.find_all('a')
  # for link in links:
  #   print(f'Link: {link["href"]}')
else:
  print(f'Failed to retrieve the webpage. Status code: {response.status_code}')