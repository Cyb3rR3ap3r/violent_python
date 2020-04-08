#!/usr/bin/python3

import zipfile

file = zipfile.ZipFile("personal.zip")
dict_file = open('dictionary.txt')

for line in dict_file.readlines():
    password = line.strip('\n')

    try:
        file.extractall(pwd=bytes(password, 'utf-8')) # convert string to bytes
        print("[+] Password = " + password + '\n')
        exit()
    except Exception as e:
        pass
