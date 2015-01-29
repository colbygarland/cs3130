#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter02/udp_remote.py
# UDP client and server for talking over the network

import argparse, random, socket, sys

MAX_BYTES = 65535

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listening at', sock.getsockname())
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')

        print('The client at {} says {!r}'.format(address, text))

        command, name = text.split(" ", 1)

       # SIGNIN COMMAND
        if command == "signin":
            print("command = " + command)
            # searches to see if person is in the system
            inDatabase = logOn(name)
            if inDatabase == True:
                message = name + " is in the database"
                # set the status to online               
                setStatusOn(name)
            else:
                message = name + " is not in the database"

       # SIGNOFF COMMAND
        elif command == "signoff":
            print("command = " + command)
            setStatusOff(name)
            message = "GoodBye"

       # WHOISON COMMAND
        elif command == "whoison":
            print("Doesn't work.\n")

       # SEND COMMAND
        elif command == "send":
            print("Doesn't work.\n")

        else:
            print("Unrecognized command")
        

        sock.sendto(message.encode('ascii'), address)


def client(hostname, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))

    print('Client socket name is {}'.format(sock.getsockname()))
    delay = 0.1 # seconds

    text = input()
    text = text.lower()

    data = text.encode('ascii')

    while True:
        sock.send(data)
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout as exc:
            delay *= 2 # wait even longer for the next request
            if delay > 2.0:
                raise RuntimeError('Not currently accepting sign-ins') from exc
        else:
            break # we are done, and can stop looping
    print('The server says {!r}'.format(data.decode('ascii')))

# logOn(name) checks with the name passed to it to see if user
# is in the database or not
def logOn(name):
    
    inFile = open("database", "r")
    inDatabase = False

    for rec in inFile:
        status, username = rec.split(":", 1)
        username, rest = username.split("\n", 1)

        if name == username:
            inDatabase = True
            break
        else:
            inDatabase = False

    inFile.close()
    return inDatabase

# Setstatuson searches for the name and changes the status in
# the database to on instead of off
def setStatusOn(name):

    searchString = "off:" + name
    with open("database", "r+") as inoutfile:
        lines = [line.replace(searchString, "on:" + name) for line in inoutfile]
        inoutfile.seek(0)
        inoutfile.truncate()
        inoutfile.writelines(lines)

# Setstatusoff searches for the name and changes the status in
# the database to off instead of on
def setStatusOff(name):

    searchString = "on:" + name
    with open("database", "r+") as inoutfile:
        lines = [line.replace(searchString, "off:" + name) for line in inoutfile]
        inoutfile.seek(0)
        inoutfile.truncate()
        inoutfile.writelines(lines)





# Prints out all the names that are online!!
def whoIsOn():

    inFile = open("database", "r")
    for rec in inFile:
        status, username = rec.split(":", 1)

        #if status == "on":
            





if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP,'
                                    ' pretending packets are often dropped')
    parser.add_argument('role', choices=choices, help='which role to take')
    parser.add_argument('host', help='interface the server listens at;'
                                    ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
    help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
