#!/usr/bin/env python3

"""First lab for cs3130
   Author: Colby Garland id# 5034957
   Employee Database"""

import database

def main():
    input_menu()
   

#Prints the menu
def print_menu():
    print("----------Employee FMS - Main Menu----------\n")

    print("Select one of the following:\n")

    print("  1) Add a new employee")
    print("  2) Search for an employee")
    print("  3) Remove an employee from FMS")
    print("  4) Display entire employee FMS")
    print("  5) Quit\n")

    print("Option: ")

#Receives the input and deals with it properly
def input_menu():
    while True:
            print_menu()
            numIn = input()
            if numIn:
                try:
                    numIn = int(numIn)
                    if numIn == 1:
                        database.add_employee()
                        continue
                    elif numIn == 2:
                        database.search_employee()
                        continue
                    elif numIn == 3:
                        database.remove_employee()
                        continue
                    elif numIn == 4:
                        database.display_all()
                        continue
                    elif numIn == 5:
                        break
                    else:
                        print("Option not valid - try again")
                        continue
                except ValueError as err:
                    print("Option not a number - try again")
                
        

#call the main which starts the program
main()
