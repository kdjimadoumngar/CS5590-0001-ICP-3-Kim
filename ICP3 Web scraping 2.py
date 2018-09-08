

import urllib.request
from bs4 import BeautifulSoup
import os

# html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
#
# bsObj = BeautifulSoup(html.content, "html.parser")
#
# print(bsObj.h1)
#
# print(bsObj.title) # To print the title
#
# print(bsObj.find_all('a') # To print all the hyperlinks
#
# for link in bsObj.find_all('a'):
#
#     print(link.get('href'))




url = "https://en.wikipedia.org/wiki/Deep_learning"

source_code = urllib.request.urlopen(url)

soup = BeautifulSoup(source_code, "html.parser")



#url = BeautifulSoup(html.content, "html.parser")

print(soup.h1.text)

print(soup.title.text) # To print the title

for link in soup.find_all('a'):

    print(link.get('href'))