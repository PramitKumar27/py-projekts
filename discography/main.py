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


def disco(url1):
    url_open = requests.get(url1)
    soup = BeautifulSoup(url_open.content, "html.parser")
    details = soup('table', {'class': 'wikitable'})
    for i in details:
        h = i.find_all('th')
        d = i.find_all('td')
        if h is not None and d is not None:
            for x, y in zip(h, d):
                print("{} :: {}".format(x.text, y.text))
                print("----------------------------------------------")


if __name__ == "__main__":
    print("Here is the basic info regarding: {0}".format(word))
    inp = input("Do you want to know basic info? Y/N ")
    if inp == "Y":
        print("Here is the basic info regarding: {0}".format(s1))
        info(url)
    inp1 = input("Do you want to know discography? Y/N ")
    if inp1 == "Y":
        print("Here is {}'s discography :: ".format(s1))
        disco(url1)
