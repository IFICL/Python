#!/usr/bin/python3.5
#Filename:continue.py

while True:
	s = input("Enter something: ")
	if s == "quit":
		break
	if len(s) < 3:
		continue

	print("The length of string is enough!")

print("Finish!")
#	when we use 'continue', it will ingore the rest part of 
#	while loop, and continue to run the while loop
