import requests
from bs4 import BeautifulSoup
import string

s0 = input("Search for : ")
s = string.capwords(s0)
s1 = s.split()
word = "_".join(s1)

url = "https://en.wikipedia.org/wiki/"+word
url1 = "http://en.wikipedia.org/wiki/"+word+"_discography#Studio_albums"


def info(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, "html.parser")
    details = soup('table', {'class': 'infobox'})
    for i in details:
        h = i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading is not None and detail is not None:
                for x, y in zip(heading, detail):
                    print("{} :: {}".format(x.text, y.text))
                    print("-------------------------------")
    for i in range(1, 3):
        print(soup('p')[i].text)


if __name__ == "__main__":
    print("Here is the basic info regarding: {0}".format(word))
    info(url)
