import requests
from bs4 import BeautifulSoup
import re
from lxml.html import fromstring
import lxml.html as PARSER

with open("fullname.html") as fp:
    soup = BeautifulSoup(fp, "lxml")

# this flip lastname, firstname to firstname lastname
 
soup = BeautifulSoup(open("fullname.html"), "lxml")

empty_arr = []

data = []
table = soup.find('table')
table_body = table.find('tbody')
allprojects = table_body.find_all("a", text=True)
# rows = table_body.find_all('tr')

for i, allprojects in enumerate(allprojects):

    empty_arr.append(str(allprojects.string))

# print (table_body)
for fl in empty_arr:

    last, first = fl.split(', ')

    tmp = first + last
    modified = tmp.replace("  ", " ")
    print(modified)

    # seperator = ' '
    # x = seperator.join([first, last])
    # print (x)

    # 
    # seperator.join(tmp1)
    # print (tmp1)


# fullname = soup.find_all("a")
# print (table_body.string)