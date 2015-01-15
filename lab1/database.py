#!/usr/bin/env python3

"""Deals with the database stuff from lab 1 
   Author: Colby Garland id# 5034957"""

#Paints the add employee page, and then asks user to enter an employee
def add_employee():
    print("\n----------Employee FMS - Add a new employee----------")
   
    while True:
        success = True
        infile = open("test", "r")
        print("\nEnter a user id, first name, last name and department as so:")
        print("--userID:fname:lname:department--\n")

        record = input()

        userID, fname, lname, dept = record.split(":")
        userID = int(userID)

        for rec in infile:
            ID, rest = rec.split(":", 1)
            ID = int(ID)
            if ID == userID:
                success = False
                
        if success:
            infile.close()
            infile = open("test", "a")
            infile.write(str(userID) + ":" + fname + ":" + lname + ":" + dept + "\n")
            infile.close()
            print("\nAddition Successful")
        else:
            infile.close()
            print("\nEmployee already in database")

        print("Do you wish to add another employee?")
        print("Enter y for yes, n to return to main menu")
        addAnother = input()
        if addAnother[0] == 'n' or addAnother[0] == 'N':
            break

#Searches for an employee
def search_employee():
    print("\n----------Employee FMS - Searching for Employee----------")

    while True:
        print("Enter an ID to search for:")
        try:
            ID = input()
            ID = int(ID)
        except ValueError as err:
            print("Employee ID must be a number.")
            continue
 
        infile = open("test", "r")

        for rec in infile:
            userID, rest = rec.split(":", 1)
            userID = int(userID)
            if ID == userID:
                fname, lname, dept = rest.split(":")
                print("\nUserID:" + str(ID) + " " + fname + " " + lname + " " + dept + "\n")
                break
            else:
                print("\nUserID:" + str(ID) + " does not exist.")
                break

        print("\nWould you like to search for another employee?")
        print("Enter y for yes, n to return to main menu")
        addAnother = input()
        if addAnother[0] == 'n' or addAnother[0] == 'N':
            inline.close()
            break

#Removes an employee specified by the user id
def remove_employee():
    print("\n----------Employee FMS - Remove Employee----------\n")
   
   
    while True:
        deleteOkay = False
        print("Enter the Employee ID to remove:")
        try:
            ID = input()
            ID = int(ID)
        except ValueError as err:
            print("Employee ID must be a number.")
            continue

        f = open("test", "r")
        for rec in f:
            searchID, rest = rec.split(":",1)
            searchID = int(searchID)
            if searchID == ID:
                deleteOkay = True
                break
        f.close()

        if deleteOkay:
            print("Employee found - are you sure you wish to delete?")
            print("Enter y for yes, n to return to main menu")
            yes = input()
            if yes[0] == 'n' or yes[0] == 'N':
                break

        if deleteOkay:
            f = open("test", "r")
            lines = f.readlines()
            f.close()
            f = open("test", "w")
            ID = str(ID)
            for line in lines:
                userID, rest = lines.split(":",1) #fix this part
                if userID != ID:
                    f.write(line)
            f.close()
            break
        else:
            print("Employee ID not in system - cannot delete")
                


#Prints the database 
def display_all():
    inline = open("test", "r")
    print("\nEmployees in the database:\n")
    for rec in inline:
        ID, fname, lname, dept = rec.split(":")
        print(ID, fname, lname, dept, end="")
    inline.close()
    print("\n")
















if __name__ == '__main__':
    add_employee()

