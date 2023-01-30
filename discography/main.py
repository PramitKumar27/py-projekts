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
    s = soup.find_all('caption')
    for caption in s:
        if 'studio albums' in caption.get_text():
            table = caption.find_parent(
                'table', {'class': 'wikitable plainrowheaders'})
            r = table.find_all('tr')
            a = 0
            for i in r:
                h = i.find_all('th')

                for x in h:
                    if a > 0:
                        if "[" not in x.text:
                            if x is not None:
                                print("{} :: ".format(x.text))
                                print("---------------")
                    if "Certifications" in x.text:
                        a = 1


if __name__ == "__main__":

    inp = input("Do you want to know basic info? Y/N ")
    if inp == "Y":
        print("Here is the basic info regarding: {0}".format(word))
        info(url)
    inp1 = input("Do you want to know discography? Y/N ")
    if inp1 == "Y":
        print("Here is {0}'s discography :: ".format(word))
        disco(url1)
