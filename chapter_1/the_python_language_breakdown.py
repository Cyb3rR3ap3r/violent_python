#!/usr/bin/python3

# For proof of concept and to keep everything clean, you will see
# multiple variables called with same name and value.
# This is just to keep everything organized.

def newline():      # Function for new line
    print("\n")

########## Variables ##########
'''
In Python, a variable points to data stored in a memory location.
This memory location can store different values such as integers, real numbers,
Booleans, strings, or more complex data such as lists or dictionaries.

In the following code, we define a variable port that stores an integer and
banner that stores a string.
To combine the two variables together into one string, we must explicitly cast
the port as a string using the str() function.
'''
port = 21
banner = "FreeFloat FTP Server"
print("[+] Checking for " + banner + " on port " + str(port))

newline()

'''
Python reserves memory space for variables when the programmer declares
them.
The programmer does not have to explicitly declare the type of variable;
rather, the Python interpreter decides the type of the variable and how much
space in the memory to reserve.

Considering the following example, we declare a string, an integer, a list, and
a Boolean, and the interpreter correctly automatically types each variable.
'''
banner = "FreeFloat FTP Server"   # String
port = 21                         # Integer
port_list = [21,22,80,110]        # List
port_open = True                  # Boolean

print(type(banner))
print(type(port))
print(type(port_list))
print(type(port_open))

newline()

########## Strings ##########

'''
The Python string module provides a very robust series of methods for strings.

Read the Python documentation at http://docs.python.org/library/string.html
for the entire list of available methods. Let’s examine a few useful methods.

Consider the use of the following methods:
upper(), lower(), replace(), and find().

Upper() converts a string to its uppercase variant.
Lower() converts a string to its lowercase variant.
Replace(old,new) replaces the old occurrence of the substring old with the
                 substring new.
Find() reports the offset where the first occurrence of the substring occurs.
'''
banner = "FreeFloat FTP Server"

print(banner.upper())
print(banner.lower())
print(banner.replace("Freefloat", "Ability"))
print(banner.find("FTP"))

newline()


########## Lists ##########

'''
The list data structure in Python provides an excellent method for storing
arrays of objects in Python.
A programmer can construct lists of any data type.
Furthermore, built-in methods exist for performing actions such as appending,
inserting, removing, popping, indexing, counting, sorting, and reversing lists.

Consider the following example:
A programmer can construct a list by appending items using the append() method,
print the items, and then sort them before printing again.

The programmer can find the index of a particular item (the integer 80 in this
example).
Furthermore, specific items can be removed (the integer 443 in this example).
'''
port_list = []
port_list.append(21)
port_list.append(80)
port_list.append(443)
port_list.append(25)

print(port_list)

port_list.sort()
print(port_list)     # List should now be sorted

pos = port_list.index(80)
print("[+] There are " + str(pos) + " ports to scan before 80.")

port_list.remove(443)
print(port_list)

cnt = len(port_list)
print("[+] Scanning " + str(cnt) + " Total Ports.")

newline()


########## Dictionaries ##########

'''
The Python dictionary data structure provides a hash table that can store
any number of Python objects.
The dictionary consists of pairs of items that contain a key and value.

Let’s continue with our example of a vulnerability scanner to illustrate a
Python dictionary.
When scanning specific TCP ports, it may prove useful to have a dictionary that
contains the common service names for each port.
Creating a dictionary, we can lookup a key like ftp and return the associated
value 21 for that port.

When constructing a dictionary, each key is separated from its value by a colon,
and we separate items by commas.
Notice that the method .keys() will return a list of all keys in the dictionary
and that the method .items() will return an entire list of items in the
dictionary.
Next, we verify that the dictionary contains a specific key (ftp).
Referencing this key returns the value 21.
'''
services = {"ftp":21, "ssh":22, "smtp":25, "http":80}

print(services.keys())   # Prints the keys only
print(services.items())  # Prints entire list with keys

print(services["ftp"])

print("[+] Found vuln with FTP on port " + str(services["ftp"]))

newline()


########## Networking ##########

'''
The socket module provides a library for making network connections using
Python.

Let’s quickly write a banner-grabbing script. Our script will print the
banner after connecting to a specific IP address and TCP port.
After importing the socket module, we instantiate a new variable s from the
class socket class.
Next, we use the connect() method to make a network connection to the IP address
and port.
Once successfully connected, we can read and write from the socket.
'''
#import socket
#socket.setdefaulttimeout(2)
#s = socket.socket()
#s.connect(("192.168.95.148, 21"))
#ans = s.recv(1024)
#print(ans)

#Will Return...
#220 FreeFloat Ftp Server (Version 1.00)



########## Selection ##########

'''
Like most programming languages, Python provides a method for conditional
select statements.
The IF statement evaluates a logical expression in order to make a decision
based on the result of the evaluation.

Continuing with our banner-grabbing script, we would like to know if the
specific FTP server is vulnerable to attack.

To do this, we will compare our results against some known vulnerable FTP
server versions.
'''
#import socket
#socket.setdefaulttimeout(2)
#s = socket.socket()
#s.connect(("192.168.95.148, 21"))
#ans = s.recv(1024)
#if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    #print "[+] FreeFloat FTP Server is vulnerable"
#elif ("3Com 3CDaemon FTP Server (Version 2.0)" in banner):
    #print "[+] FreeFloat FTP Server is vulnerable"
#if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    #print "[+] FreeFloat FTP Server is vulnerable"
#if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    #print "[+] FreeFloat FTP Server is vulnerable"










# Space
