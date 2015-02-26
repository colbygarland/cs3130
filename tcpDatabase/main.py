#!/usr/bin/env python3

"""4th lab for cs3130
   Author: Colby Garland id# 5034957
   Employee Database TCP"""

import socket, argparse, struct, sys
End = '.'


#Paints the add employee page, and then asks user to enter an employee
def add_employee():
    print("\n----------Employee FMS - Add a new employee----------")
    message = "+200:"
   
    print("\nEnter a user id, first name, last name and department as so:")
    print("    userID:fname:lname:department    \n")

    print("> ", end="")
    message += input()
    message += End

    return message


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

        message = '+300:' + str(ID) + End
        break

    return message
       

  

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

        message = '+400:' + str(ID) + End
        break

    return message



def recvall(the_socket):
    total_data=[];data=''
    while True:
            data=the_socket.recv(8192)
            data = data.decode('utf-8')
            if End in data:
                total_data.append(data[:data.find(End)])
                break
            total_data.append(data)
            if len(total_data)>1:
                #check if end_of_data was split
                last_pair=total_data[-2]+total_data[-1]
                if End in last_pair:
                    total_data[-2]=last_pair[:last_pair.find(End)]
                    total_data.pop()
                    break
    return ''.join(total_data)




# Client side
def client(host, port):

   # pg 66 getaddrinfo not web, 2015 in book



    message = ""

    while True:
        print_menu()
        numIn = input()
        if numIn:
            try:
                numIn = int(numIn)
                if numIn == 1:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((host,port))
                    message = add_employee()
                    encoded = bytes(message, 'utf-8')
                    sock.sendall(encoded)
                    reply = recvall(sock)
                    sock.close()
                    print(repr(reply))
                    continue
                elif numIn == 2:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((host,port))
                    message = search_employee()
                    encoded = bytes(message, 'utf-8')
                    sock.sendall(encoded)
                    reply = recvall(sock)
                    sock.close()
                    print(repr(reply))
                    continue
                elif numIn == 3:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((host,port))
                    message = remove_employee()
                    encoded = bytes(message, 'utf-8')
                    sock.sendall(encoded)
                    reply = recvall(sock)
                    sock.close()
                    print(repr(reply))
                    continue
                elif numIn == 4:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((host,port))
                    message = '+500.'
                    encoded = bytes(message, 'utf-8')
                    sock.sendall(encoded)
                    reply = recvall(sock)
                    print(repr(reply))
                    sock.close()
                    continue
                elif numIn == 5:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((host,port))
                    sock.close()
                    break
                else:
                    print("Option not valid - try again")
                    continue
            except ValueError as err:
                print("Option not a number - try again")





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
        
        if '+200' in message: # add employee!!
            success = True
            code, userID, fname, lname, dept = message.split(':')
            print('Code   = ' + code)
            print('UserID = ' + userID)
            print('Fname  = ' + fname)
            print('Lname  = ' + lname)
            print('Dept   = ' + dept)

            infile = open('database', 'r')
            for rec in infile:
                ID, rest = rec.split(':', 1)
                if ID == userID:
                    success = False
                    infile.close()
                    break
            
            if success:
                infile = open('database', 'a')
                infile.write(userID + ':' + fname + ':' + lname + ':' + dept + '\n')
                infile.close()
                sc.sendall(b'----Addition Successful.')
            else:
                sc.sendall(b'Employee is already in database.')

        elif '+300' in message: # search employee
            check = False
            code, ID = message.split(':', 1)
            infile = open('database', 'r')
         
            for rec in infile:
                userID, rest = rec.split(':', 1)
                if ID == userID:
                    fname, lname, dept = rest.split(':')
                    sc.sendall(b'UserID: ' + bytes(fname, 'utf-8') + b' ' + bytes(lname, 'utf-8') + b' ' + bytes(dept, 'utf-8') + b'.')
                    check = True
                    break

            if check == False:
                sc.sendall(b'User does not exist.')

        elif '+400' in message: # remove employee
            searchString = ''
            deleteOkay = False
            code, ID = message.split(':', 1)
            infile = open('database', 'r')
          
            for rec in infile:
                searchString = rec
                searchID, rest = rec.split(':', 1)
                if searchID == ID:
                    deleteOkay = True
                    sc.sendall(b'Employee deleted.')
                    infile.close()
                    break

            if deleteOkay:
                with open("database", "r+") as inoutfile:
                    lines = [line.replace(searchString, "") for line in inoutfile]
                    inoutfile.seek(0)
                    inoutfile.truncate()
                    inoutfile.writelines(lines)
            else:
                sc.sendall(b'Employee ID not in system - cannot delete.')

        elif '+500' in message: # display all employees
            inline = open("database", "r")
            emptiness = True
            message = 'Employees in Database:\n'
            for rec in inline:
                ID, fname, lname, dept = rec.split(":")
                message += ID + fname + lname + dept + '\n'
                emptiness = False

            if emptiness:
                message = b'Employee database is currently empty.'
            else:
                message += End

            inline.close()
            sc.sendall(bytes(message, 'utf-8'))            

        #sc.sendall(b'Farewell, client.')
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
