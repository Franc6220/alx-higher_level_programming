#!/usr/bin/python3
def fizzbuzz():
  for a in range(1, 100):
      if a % 3 == 0 and a % 5 != 0:
         print("{}Fizz ", end = ''.format(a))
      elif a % 5 == 0 and a % 3 != 0:
         print("Buzz ", end = '')
      elif a % 3 == 0 and a % 5 == 0:
         print("FizzBuzz ", end = '')
  else:
       print(f'{a}', end = '')      
