# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 6, 11, 12, "apple", "bananna"]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "apple", "bananna"]
c = []
count = 0
if len(a) > len(b):
    for i in a:
        if i in a and i in b:
            c.append(i)
            count += 1
        else:
            continue
else:
    for i in b:
        if i in a and i in b:
            c.append(i)
            count += 1
        else:
            continue
print("The common part in a and b are", c)
print("The number of common part is", count)