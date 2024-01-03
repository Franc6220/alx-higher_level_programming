#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num1 = number-(int(number/10)*10)
#if last digit is greater than five
if number > 5:
   print('Last digit of {number} is {num1} and is greater than 5'.format(number = "random.randint(-10000, 10000)", num1 = "number-(int(number/10)*10)"))
#if last digit is zero
elif number == 0:
   print('Last digit of {number} is {num1} and is 0'.format(number = "random.randint(-10000, 10000)", num1 = "number-(int(number/10)*10)"))
#if last digit is less than 6 and not zero
elif number < 6 and not number == 0:
   print('Last digit of {number} is {num1} and is less than 6 and not 0'.format(number = "random.randint(-10000, 10000)", num1 = "number-(int(number/10)*10)"))
