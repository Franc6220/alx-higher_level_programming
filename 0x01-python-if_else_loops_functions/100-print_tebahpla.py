#!/usr/bin/python3
# Python3 program to print alphabets

# Function to print the alphabet
# in lower case
def lowercaseAlphabets():

	# lowercase
	for c in range(97, 123):
		print(chr(c), end = " ");

	print("");

# Function to print the alphabet
# in upper case
def uppercaseAlphabets():

	# uppercase
	for c in range(65, 91):
		print(chr(c), end = " ");

	print("");

print("Uppercase Alphabets");
uppercaseAlphabets();

print("Lowercase Alphabets ");
lowercaseAlphabets();


