#!/usr/bin/python

a = 7
c = 3

while c > 0:
        number = int(input("Please input a number: ")
	if number > a:
		print("Too Big")
	elif number < a:
		print("Too small")
	else:
		print("Yes, you did it")
		break
	c -= 1
	print("You have " + str(c) + " chances left. ")
print("Have Fun")
