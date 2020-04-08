#!/usr/bin/python3

import zipfile

def extract_file(zip_file, password):
    try:
        file.extractall(pwd=bytes(password, 'utf-8')) # convert string to bytes
        return password
    except:
        return

def main():
    zip_file = zipfile.ZipFile("personal.zip")
    dict_file = open('dictionary.txt')
    for line in dict_file.readlines():
        password = line.strip('\n')
        guess = extract_file(zip_file, password)
        if guess:
            print("[+] Password = " + password + '\n')
            exit()

if __name__ == '__main__':
    main()

# Not working 




'''

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

'''
