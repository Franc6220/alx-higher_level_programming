#!/usr/bin/python3
def uppercase(str):
    for n in str:
        temp = n
        if ord(n) >= 97 and ord(n) <= 122:
           temp = chr(ord(n) - 32)
        print("{}".format(temp), end='')
    
