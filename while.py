#!/usr/bin/python3.5
#Filename:while.py

number = 23
guess = 0

while guess != number:
	guess = int(input("Enter an integer: "))

	if guess == number:
		print("Congratulations!")
		#break
	elif guess > number:
		print("No, it's lower than that.")
	else:
		print("No, it's higer than that.")
else:
	print("Game over!")

#while loop
#if we have "break", it will not run to else part(while)