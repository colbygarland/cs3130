#!/usr/bin/env python3

"""Project for CS3130
   Author: Colby Garland
   ID#   : 5034957

   Simulate an online store using udp

   All the interface code"""

# Prints the menu, accepts input and returns option number
def client_menu():
    print("--Welcome to Colby's Online Store\n")
    print('Options:')
    print('        1. Browse the Store')
    print('        2. Log in to account')
    print('        3. Review cart')
    print("        4. Exit Colby's Online Store")

    # Makes sure input is a number
    correct_input = 1
    while(correct_input):
        print('> ', end="")
        option = input()
        try:
            numOption = int(option)
            if numOption > 4 or numOption < 1:
                print('Option not a valid option - try again')
            else:
                correct_input = 0
        except ValueError:
            print('Option not recognized - try again')

    return option

# 1. Browse the Store
def browse_store(user):
    message = ''

    if user != '':
        message = '\n--Welcome, ' + user + '\n'
    else:
       message = '\n--Welcome, Guest\n'

    message += '\n--Products in Store\n'
    message += '--------------------------------------------------------------------------------'
    
    allProducts = open('product_database', 'r')
    for product in allProducts:
        pn, pname, pm = product.split(':')
        message += '    ' + 'Product Number: ' + pn + '  Product Name: ' + pname + '  Company: ' + pm
        message += '--------------------------------------------------------------------------------'
    allProducts.close()

    return message

# 2. login prompt username
def login_prompt_username():
    message = '--Login'
    message += '\n--Enter Username: '
    return message

# 2. login prompt password
def login_prompt_password():
    message = '--Enter Password: '
    return message

#4. Exit shop
def exit_store(user):
    if user != '':
        message = '--We will miss your business, ' + user + '!'
    else:
        message = '--We will miss your business, Guest!'
    message += '\n--Goodbye!'
    return message





















