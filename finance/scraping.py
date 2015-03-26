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
    return r.text

# searches the text for the gold stock
def goldStock():
    print('Gold ', end = '')
    text = getText()

    rx = r'</span>\d+\,\d+\.\d+'
    prog = re.compile(rx)
    
    for match in prog.finditer(text):
        s = match.group(0)
        #print(s)

    



# finds the s & p stock info
def spStock():
    print('S & P TSX ', end='') 
    r = getRequest()
 

    # this regex gets all info for the stock
    rx = r'<div data-id="593253" .*?</span></div></div></td>'
    prog = re.compile(rx)

    # gets the first number
    rx2 = r'\d+\,\d+\.\d+'
    prog2 = re.compile(rx2)

    rx4 = r'\d+\:\d+ (P|A)M EDT'
    prog4 = re.compile(rx4)

    rx5 = r'[\-\+]\d+\.\d+'
    prog5 = re.compile(rx5)

    s = ''
    for match in prog.finditer(r.text):
        s = match.group(0)
        #print(s)

    for match in prog2.finditer(s):
        t = match.group(0)
        print(t + ' ', end = '')

    for match in prog5.finditer(s):
        t = match.group()
        print(t + ' ', end = '')

    print('%', end = ' ')


    for match in prog4.finditer(s):
        t = match.group(0)
        print(t)

    

























