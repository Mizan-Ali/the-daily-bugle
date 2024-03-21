import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://indianexpress.com/todays-paper/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div with class "section ev-meter-content"
div_section = soup.find('div', class_='section ev-meter-content')

# Find all the <li> tags within the div
list_items = div_section.find_all('li')

# Extract the href attribute from the first <a> tag within each <li> tag and print
for li in list_items:
    link = li.find('a')
    if link:
        href = link.get('href')
        print(href)
