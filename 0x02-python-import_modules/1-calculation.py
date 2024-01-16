#!/usr/bin/python3
if _name_ == "_main_":
   """print math calculation of a and b"""
   from calculator_1 import ccalculator
        
        a = 10
        b = 5

        print("{} + {} = {}".format(a, b, add(a, b)))
        print("{} - {} = {}".format(a, b, sub(a, b)))
        print("{} * {} = {}".format(a, b, mul(a, b)))
        print("{} / {} = {}".format(a, b, div(a, b)))
