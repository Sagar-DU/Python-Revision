# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input ("Enter your name: ")
age = input ("Enter your age: ")

import datetime

today = datetime.datetime.now()

#accessing the year attribute
year = today.year

year100 = year + (100 - int(age))

print(name, "will be 100 years old in ", year100)