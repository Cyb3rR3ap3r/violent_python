#!/usr/bin/python3

import crypt
import time
# More info on the crypt library here:
#     https://docs.python.org/3/library/crypt.html

word = input("[+] Enter your password: ")

def create_hash ():
    print("[-] Which hashing algorithm?")
    print("[-]   1 = SHA-512    2 = SHA-256")
    print("[-]   3 = BLOWFISH   4 = MD5")
    choice = input("[+] ")

    if choice == "1":
        salt = crypt.METHOD_SHA512
    elif choice == "2":
        salt = crypt.METHOD_SHA256
    elif choice == "3":
        salt = crypt.METHOD_BLOWFISH
    elif choice == "4":
        salt = crypt.METHOD_MD5
    else:
        print("Incorrect value.  Please retry.")
        create_hash()
    hash = crypt.crypt(word, salt)
    print(hash)


create_hash()
