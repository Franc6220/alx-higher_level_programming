#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#If number is greater than zero
if number > 0:
  print("{} is positive\n".format(**number))

#If number is zero
elif number == 0:
   print("{} is zero\n".format(**number))

#If number is less than zero
elif number < 0:
   print("{} is negative\n".format(**number))

