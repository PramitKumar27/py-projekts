import requests
from bs4 import BeautifulSoup
import string

s0 = input("Search for : ")
s = string.capwords(s0)
s1 = s.split()
word = "_".join(s1)

print(word)
