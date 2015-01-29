#!/usr/bin/env python3

""" Messenger Lab for cs3130 Lab3
    Sending messages over the network using udp
    Author: Colby Garland 
    ID#   : 5034957 """

import udp_remote

def main():
    beginningScreen()


# Prints out the main screen
def beginningScreen():

    print("--")
    print("Welcome to MMS")
    print("------------------------------------")
    print("The following commands are supported:")
    print("    signin <username>")
    print("    whoIsOn")
    print("    send <username> <message>")
    print("    signout")


# Accepts the input to determine what to do
def input_menu():

    while True:
        print("> ", end="")
        text = input()
        text = text.lower()
        
            



main()
