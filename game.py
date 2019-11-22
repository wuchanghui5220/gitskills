#!/usr/bin/python

a = 7
c = 3

# print(type(number))
while c > 0:
    number = int(input("Please input a number: "))
    if number == a:
        print("Yes, you did it")
        break
    elif number <= a:
        print("Too small")
    else:
        print("Too Big")
    c -= 1
    print("You have " + str(c) + "chances left. ")
