import requests
from bs4 import BeautifulSoup

req = requests.get("https://8marketcap.com/")
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.find_all('th'))