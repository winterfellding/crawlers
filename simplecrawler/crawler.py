"""
Crawler V0.1

This is a simple web crawler for download image file from the page,
using beautiful soup4 for query the right element of html, 
and wget for downloading file
"""

import wget
import urllib.request
from bs4 import BeautifulSoup

def downloadFile(url):
    """"
    When download hangs, the program stops.
    It's a bug.
    """
	f = wget.download(url)
	print(str(f) + " is downloaded")

start_url='http://START_URL'


def findAllPics(url):
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    for link in soup.findAll('img', src=True):
        """
        only download the right picture by the file url.
        """
        if link['src'].count('site_you_want_to_find') > 0:
            downloadFile(link['src'])
    return soup

while True:
    soup = findAllPics(start_url)
    li = soup.find('li', {'class': 'next'})
    start_url = li.find('a')['href']
