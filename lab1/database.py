#!/usr/bin/env python3

"""Deals with the database stuff from lab 1 
   Author: Colby Garland id# 5034957"""

#Paints the add employee page, and then asks user to enter an employee
def add_employee():
    print("\nEmployee FMS - Add a new employee")
    
    inputCheck = True
    success = False
    

    while True:
        infile = open("test", "r")
        print("\nEnter a user id, first name, last name and department as so:")
        print("userID:fname:lname:department\n")

        record = input()

        userID, fname, lname, dept = record.split(":")
        userID = int(userID)

        for rec in infile:
            ID, rest = rec.split(":", 1)
            ID = int(ID)
            if ID == userID:
                print("ID already in - try again")
                infile.close()
                success = False
                
                

        if success:
            infile.close()
            infile = open("test", "a")
            infile.write(str(userID) + ":" + fname + ":" + lname + ":" + dept + "\n")
            infile.close()
            print("\nAddition Successful")
            print("Do you wish to add another employee?")
            addAnother = input()
            if addAnother[0] == 'n' or addAnother[0] == 'N':
                break




if __name__ == '__main__':
    add_employee()

