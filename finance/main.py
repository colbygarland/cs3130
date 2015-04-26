#!/usr/bin/env python3

import scraping

"""Main program to present the menu to the user, accept input
   Author: Colby Garland
   ID#   : 5034957
   Assignment #6 CS3130"""

# calls the printmenu() and accepts input 
def menu():
    while True:
        printMenu()
        market = input()
        if market == '1':
            scraping.spStock()
            continue
        elif market == '2':
            continue
        elif market == '3':
            continue
        elif market == '4':
            continue
        elif market == '5':
            continue
        elif market == '6':
            scraping.goldStock()
        elif market == '7':
            continue
        elif market == '8':
            break



# prints the menu
def printMenu():
    print('--')
    print('Market Information\n')
    print('Select one of the following:\n')
    print('  1) S&P TSX')
    print('  2) S&P 500')
    print('  3) Dow Jones')
    print('  4) Nasdag')
    print('  5) CAD/USD')
    print('  6) Gold')
    print('  7) WTI Crude')
    print('  8) Quit\n')
    print('>>> ',end='')

menu()



