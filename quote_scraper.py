import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com'
res = requests.get(url)
if res.status_code == 200:
  soup = BeautifulSoup(res.text, 'html.parser')
  
  # Extract quotes, authors, and tags
  for quote in soup.find_all('span', class_='text'):
      print("Quote:", quote.get_text())
      print("Author:", quote.find_next('small', class_='author').get_text())
      tags = [tag.get_text() for tag in quote.find_next('div', class_='tags').find_all('a', class_='tag')]
      print("Tags:", tags)
      print("------")
else:
   print(f'Failed to retrieve webpage. Status: {res.status_code}')