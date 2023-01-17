import requests
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring
import lxml.html as PARSER

with open("fullname.html") as fp:
    soup = BeautifulSoup(fp, "lxml")

# print (soup)

soup = BeautifulSoup(open("fullname.html"), "lxml")

mydivs = soup.find_all("a", text=True)



for i, mydivs in enumerate(mydivs):
    print (str(i) + ": " + str(mydivs.string))


# fullname = soup.find_all("a")
# print (fullname.string)