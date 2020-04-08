#!/usr/bin/python3

import socket

# Uses HTB - Devel retired box (10.10.10.5)
# This is not complete.

def banner():
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect(("10.10.10.5",21))
        ans = s.recv(1024)
        print(ans)
        s.shutdown(1) # By convention, but not actually necessary
        s.close()     # Remember to close sockets after use!
    except socket.error as socketerror:
        print("Error: ", socketerror)

banner()












#Space
