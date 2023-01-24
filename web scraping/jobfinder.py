from bs4 import BeautifulSoup
import requests


html_text = requests.get("https: // www.xing.com/discover/updates").text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all(
    'li', class_='ember-view')
