# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

number = input ("Enter an integer number: ")

if int(number) % 2 == 0 :
    print ("The input number is an Even number:", number)

else:
    print ("The input number is an Odd number:", number)