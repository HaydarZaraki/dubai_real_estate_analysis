import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ayush.nz/technology")

html = response.text
print(html)