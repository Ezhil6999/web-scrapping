from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

import requests
from bs4 import BeautifulSoup

url = 'https://www.9987up.cc/#/winTrx'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
# Extract the desired data using BeautifulSoup's methods
# For example, let's extract the text from all <p> tags on the page
paragraphs = soup.find_all('p')
data = [p.text for p in paragraphs]

# Print the scraped data
for d in data:
    print(d)

# Extract the desired data using BeautifulSoup's methods
# For example, let's extract the text from all <p> tags on the page
paragraphs = soup.find_all('p')
data = [p.text for p in paragraphs]

# Print the scraped data
for d in data:
    print(d)

#heading = soup.find('tr', class_="list_header").find_all("td")

# file = open('waste.csv', 'w', newline="");
# writer = csv.writer(file)
# head_value = []
# head_value.append('Url')
# response = requests.get("https://etenders.gov.in/eprocure/app")
# soup = BeautifulSoup(response.text, 'html.parser')
# writer.writerow()

