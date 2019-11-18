#!/usr/bin/python

a = 7
c = 3
number = int(input("Please input a number: ")

while c > 0:
	if number > a:
		print("Too Big")
	elif number < a:
		print("Too small")
	else:
		print("Yes, you did it")
		break
	c -= 1
	print("You have $c chances left. ")
