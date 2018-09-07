

import urllib.request
from bs4 import BeautifulSoup
import os


def search_spider(sea, lim):
    url = "https://en.wikipedia.org/wiki/Deep_learning"+lim+"&offset=0&search="+sea
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")
    result_list = soup.findAll('div', {'class': "mw-search-result-heading"})
    print(result_list)
    for div in result_list:
        link = div.find('a')
        href = "https://en.wikipedia.org"+link.get('href')
        if (link.get('href').startswith("http")):
            href=link.get('href')
        get_data(href)

# def get_data(url):
#     source_code = urllib.request.urlopen(url)
#     plain_text = source_code
#     soup = BeautifulSoup(plain_text, "html.parser")
#     body = soup.find('div', {'class': 'mw-parser-output'})
#     file2.write(str(body.text))
#     print(body.text)

def get_data(url):
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")
    body = soup.find('div', {'class': 'mw-parser-output'})
    file2.write(str(body.text))
    print(body.text)

search = input('type a word to search in wiki: ')

limit = input('Type the number of results you want to have: ')

if not os.path.exists(search):
    print("Creating folder " + search)
    file2 = open(search+'.txt','a+',encoding='utf-8')

search_spider(search, limit)


