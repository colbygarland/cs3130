#!/usr/bin/env python3

import requests, re

"""Does all the screen scraping/searching for the info the 
   user wants"""

# gets the request from the globeandmail website
def getRequest():
    r = requests.get('http://www.theglobeandmail.com/globe-investor/')
    return r

# get the text from the request
def getText():
    r = getRequest()
    text = r.text

# searches the text for the gold stock
def goldStock():
    text = getText()

    rx1 = r'div id="MOD"+'
    stock = re.search(rx1, text)
    print(stock.group())
            
