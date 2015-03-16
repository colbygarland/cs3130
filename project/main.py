#!/usr/bin/env python3

"""Project for CS3130
   Author: Colby Garland
   ID#   : 5034957

   Simulate an online store using udp"""

import socket, argparse, sys, client_interface
MAX_BYTES = 65535
user = ''


def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))

    while True:

        optionNumber = client_interface.client_menu()
        if optionNumber == '4':
            print(client_interface.exit_store(user))
            break

        data = optionNumber.encode('ascii')

        delay = 0.1
        while True:
            sock.send(data)
            sock.settimeout(delay)
            try:
                data = sock.recv(MAX_BYTES)
            except (ConnectionRefusedError, socket.timeout):
                print("Server currently not up")
                sys.exit(0)
            else:
                break 
        print(data.decode('ascii'))



def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listening at', sock.getsockname())

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')

        print('The client at {} says {!r}'.format(address, text))

        if text == '1':
            message = client_interface.browse_store(user)
        else:
            message = 'default val'

        try:
            sock.sendto(message.encode('ascii'), address)
        except UnboundLocalError:
            print("User didn't enter correct command")
            message = "Command not recognized"


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
