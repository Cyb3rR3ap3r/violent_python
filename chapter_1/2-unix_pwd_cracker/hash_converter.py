#!/usr/bin/python3

import crypt
import time
import sys
# More info on the crypt library here:
#     https://docs.python.org/3/library/crypt.html

retry = 0

word = input("[+] Enter your password: ")
print("[-] Which hashing algorithm?")
print("[-]   1 = SHA-512    2 = SHA-256")
print("[-]   3 = BLOWFISH   4 = MD5")


def create_hash ():
    global retry
    choice = input("[+] ")
    print("\n")
    if choice == "1":
        salt = crypt.METHOD_SHA512
    elif choice == "2":
        salt = crypt.METHOD_SHA256
    elif choice == "3":
        salt = crypt.METHOD_BLOWFISH
    elif choice == "4":
        salt = crypt.METHOD_MD5
    else:
        if retry < 2:
            print("Incorrect value.  Please retry.")
            retry += 1
            create_hash()
        else:
            print("3 Failed attempts.  Exiting program.")
            sys.exit()
    hash = crypt.crypt(word, salt)
    print(hash)


create_hash()
