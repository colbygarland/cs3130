#!/usr/bin/env python3

"""4th lab for cs3130
   Author: Colby Garland id# 5034957
   Employee Database TCP"""

import socket, argparse


#Paints the add employee page, and then asks user to enter an employee
def add_employee():
    print("\n----------Employee FMS - Add a new employee----------")
   
    while True:
        success = True
        #infile = open("database", "r")
        print("\nEnter a user id, first name, last name and department as so:")
        print("    userID:fname:lname:department    \n")

        print("> ", end="")
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
            infile = open("database", "a")
            infile.write(str(userID) + ":" + fname + ":" + lname + ":" + dept + "\n")
            infile.close()
            print("\n----Addition Successful.")
        else:
            infile.close()
            print("\nEmployee is already in database.")

        print("Do you wish to add another employee?")
        print("Enter 'y' for yes, 'n' to return to Main Menu.")
        addAnother = input()
        if addAnother[0] == 'n' or addAnother[0] == 'N':
            break

#Searches for an employee
def search_employee():
    print("\n----------Employee FMS - Searching for Employee----------")
    

    while True:
        check = False
        print("Enter an ID to search for: ", end="")
        try:
            ID = input()
            ID = int(ID)
        except ValueError as err:
            print("EMPLOYEE ID MUST BE A NUMBER.")
            continue
 
        infile = open("database", "r")

        for rec in infile:
            userID, rest = rec.split(":", 1)
            userID = int(userID)
            if ID == userID:
                fname, lname, dept = rest.split(":")
                print("\nUser:" + str(ID) + " " + fname + " " + lname + " " + dept)
                check = True
                break

        if check == False:
           print("\nUserID:" + str(ID) + " does not exist.\n")

        print("Would you like to search for another employee?")
        print("Enter 'y' for yes, 'n' to return to Main Menu.")
        print("> ", end = "")
        addAnother = input()
        if addAnother[0] == 'n' or addAnother[0] == 'N':
            infile.close()
            break

#Removes an employee specified by the user id
def remove_employee():
    print("\n----------Employee FMS - Remove Employee----------\n")
    searchString = ""
   
    while True:
        deleteOkay = False
        print("Enter the Employee ID to remove: ", end="")
        try:
            ID = input()
            ID = int(ID)
        except ValueError as err:
            print("Employee ID must be a number.")
            continue

        f = open("database", "r")
        for rec in f:
            searchString = rec
            searchID, rest = rec.split(":",1)
            searchID = int(searchID)
            if searchID == ID:
                deleteOkay = True
                break
        f.close()

        if deleteOkay:
            print("Employee found - Are you sure you wish to delete?")
            print("Enter 'y' for yes, 'n' to return to Main Menu.")
            print("> ", end="")
            yes = input()
            if yes[0] == 'n' or yes[0] == 'N':
                break

        if deleteOkay:
            with open("database", "r+") as inoutfile:
                lines = [line.replace(searchString, "") for line in inoutfile]
                inoutfile.seek(0)
                inoutfile.truncate()
                inoutfile.writelines(lines)
            break
        else:
            print("Employee ID not in system - cannot delete")
            break
                


#Prints the database 
def display_all():
    inline = open("database", "r")
    emptiness = True
    print("\nEmployees in the database:\n")
    for rec in inline:
        ID, fname, lname, dept = rec.split(":")
        print(ID, fname, lname, dept, end="")
        emptiness = False

    if emptiness:
        print("Employee database is currently empty.\n")

    inline.close()
    print("\n")



def recvall(sock):
    data = b''
    while True:
        more = sock.recv(1)
        if more == '.':
            break
        data += more
    return data



# Client side
def client(host, port):

   # pg 66 getaddrinfo not web, 2015 in book

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))

    input_menu()





# Server side
def server(interface, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)

    print('Server listening at', sock.getsockname())
    while True:
        print('Waiting to accept a new connection')
        sc, sockname = sock.accept()
        print('Accepted a connection from', sockname)
        message = recvall(sc)
        print('Message = ', repr(message))

        





        sc.sendall(b'Farewell, client')
        sc.close()
        print('Reply sent, socket closed')
















#Prints the menu
def print_menu():
    print("----------Employee FMS - Main Menu----------\n")

    print("Select one of the following:\n")

    print("  1) Add a new employee")
    print("  2) Search for an employee")
    print("  3) Remove an employee from FMS")
    print("  4) Display entire employee FMS")
    print("  5) Quit\n")

    print("Option: ", end="")

#Receives the input and deals with it properly
def input_menu():
    while True:
            print_menu()
            numIn = input()
            if numIn:
                try:
                    numIn = int(numIn)
                    if numIn == 1:
                        add_employee()
                        continue
                    elif numIn == 2:
                        search_employee()
                        continue
                    elif numIn == 3:
                        remove_employee()
                        continue
                    elif numIn == 4:
                        display_all()
                        continue
                    elif numIn == 5:
                        break
                    else:
                        print("Option not valid - try again")
                        continue
                except ValueError as err:
                    print("Option not a number - try again")
                


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
    ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=2015,
    help='TCP port (default 2015)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
