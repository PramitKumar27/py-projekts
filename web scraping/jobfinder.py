from bs4 import BeautifulSoup
import requests


html_text = requests.get(
    'https://www.linkedin.com/jobs/search/?currentJobId=3446717669&keywords=python%20jobs%20berlin').text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all(
    'li', class_='ember-view')
