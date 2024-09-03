# print('Hello World')
# print(8)
# print('''
# Day 1 - Python Print Function
# The function is declared like this:
# print('what  to print')
# ''')
#
# print('hello world\nhello world' + ' hiii')
#
# print('Day 1 - String Manipulation')
# print('String Concatenation is done with the "+" sign')
# print('e.g. print("Hello " + "World")')
# print('New lines can be created with a backslash and n.')
#
# name = input("Enter your name: ")
# print(len(name))
#
# a = input()
# b = input()
#
# first = a
# second = b
#
# a = second
# b = first
#
# print('a:' + a)
# print('b:' + b)

print("Welcome to the Band Name Generator")
print('Band name should not be greater than 12 letters')
city_name = input("What's the name of the city you grew up in?\n")

pet_name = input("What's your pet's name?\n")

band_name = city_name + pet_name

if len(band_name) <= 12:
    print('Your band name could be ' + city_name + ' ' + pet_name)
else:
    print('Limit exceeded \nTry again!')
