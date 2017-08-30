#!/usr/bin/python3.5
#Filename:if.py
number = 23
guess = int(input("Enter an integer: "))

if guess == number:
	print("Congratulations!")
elif guess > number:
	print("No, it's lower than that.")
else:
	print("No, it's higer than that.")

print("Game over!")

#if loop