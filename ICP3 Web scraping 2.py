

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




url = "https://en.wikipedia.org/wiki/Deep_learning"+lim+"&offset=0&search="+sea

#url = BeautifulSoup(html.content, "html.parser")

print(url.h1)

print(url.title) # To print the title

print(url.find_all('a') # To print all the hyperlinks

for link in url.find_all('a'):

    print(link.get('href'))