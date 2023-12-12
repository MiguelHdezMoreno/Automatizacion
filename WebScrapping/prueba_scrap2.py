import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

# URL of the web page to scrape
url = "http://quotes.toscrape.com/"

# Send a GET request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Extract all the <div> tags with class 'quote' into a list object
quote_divs = soup.find_all("div", class_="quote")

# Create a list to store the quotes and authors
quotes = []

# Start with the first page
page_number = 1

while True:
    # Send a GET request to the URL
    url = f"http://quotes.toscrape.com/page/{page_number}/"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # If the page says "No quotes found!", we've reached a page that doesn't exist, so stop the loop
    if "No quotes found!" in soup.text:
        break

    # Extract all the <div> tags with class 'quote' into a list object
    quote_divs = soup.find_all("div", class_="quote")

    # Iterate over the <div> tags and get the text of the quote and the author
    for div in quote_divs:
        quote = div.find(class_='text').text
        author = div.find(class_='author').text
        quotes.append({'quote': quote, 'author': author})

    # Go to the next page
    page_number += 1

# Sort the quotes by author
quotes.sort(key=lambda x: x['author'])

# Write to .json file
with open('quotes.json', 'w', encoding='utf-8') as file:
    json.dump(quotes, file, ensure_ascii=False, indent=4)

# Write to .csv file
df = pd.DataFrame(quotes)
df.to_csv('quotes.csv', index=False, encoding='utf-8')