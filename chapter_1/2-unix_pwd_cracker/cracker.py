#!/usr/bin/python3

# This script is used to crack passwords found in the /etc/shadows file
# In Linux systems

import crypt


def test_pass(crypt_pass):

    # These are used to extract the salt from the hash in the password file
    i = crypt_pass.rfind('$')
    salt = crypt_pass[:i]

    dict_file = open('dictionary.txt','r')

    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word, salt)

        if (crypt_word == crypt_pass):
            print("[+] Found Password: " + word + "\n")
            return

    print("[-] Password Not Found.\n")
    return


def main():
    pass_file = open('password.txt')
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_pass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password for: " + user)
            test_pass(crypt_pass)

if __name__ == "__main__":
    main()
