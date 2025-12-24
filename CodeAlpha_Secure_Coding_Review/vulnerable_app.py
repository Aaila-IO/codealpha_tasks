import os
import sys

def login():
    username = raw_input("Enter username: ")
    password = raw_input("Enter password: ")

    if username == "admin" and password == "admin123":
        print("Login successful")
        command = raw_input("Enter command to execute: ")
        os.system(command)
    else:
        print("Login failed")

def read_file():
    filename = raw_input("Enter filename to read: ")
    f = open(filename, "r")
    print(f.read())
    f.close()

login()
read_file()

