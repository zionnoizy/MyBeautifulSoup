import requests
from bs4 import BeautifulSoup


page = requests.get('https://onsiteselfie.com/admin/project/', auth=('migration@companiesms.co.uk', 'cmsmigration'))
# soup = BeautifulSoup (page.content)


soup = BeautifulSoup(page.content, "lxml") # If this line causes an error, run 'pip install html5lib' or install html5lib


# wide-element-container
mydivs = soup.find_all("div", {"class": "app"})

# print(soup.prettify())

print (mydivs)