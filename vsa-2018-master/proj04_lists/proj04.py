import random
# coding=utf-8
# Name: Eliza Thornton
# Date: 7-11-18

"""
proj04

practice with lists

"""

# Part I
# Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
for m in a:
    if m < 5:
        print m

# Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
def common(a, b):
    clist = []
    if len(a) > len(b):
        for x in b:
            if x in a and x not in clist:
                clist.append(x)
    else:
        for x in a:
            if x in b and x not in clist:
                clist.append(x)
    return clist

def randlist(x):
    length = int(raw_input("How many values? "))
    low = int(raw_input("Lower number limit? "))
    while True:
        upp = int(raw_input("Upper number limit? "))
        if upp >= low:
            break
        else:
            print "Upper limit can't be lower than lower limit."
    for a in range(length):
        x.append(random.randint(low, upp))
    return x


ran_list = []
ban_list = []
print randlist(ran_list)
print randlist(ban_list)
print common(ran_list, ban_list)
# print common(b, c)

# Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.
count = 0
for item in d:
    if item == "a":
        d[count] = "*"
    print item
    count += 1
# Part IV
# Ask the user for a string, and print out whether this string is a palindrome or not
snout = str(raw_input("Give me a string and I'll tell you if it's a palindrome or not: "))
snout = snout.lower()
lista = []
listb = []
countin = len(snout) / 2 - 1
while countin >= 0:
    lista.append(snout[countin])
    countin -= 1
if len(snout) % 2 == 0:
    countin = len(snout) / 2
    while countin < len(snout):
        listb.append(snout[countin])
        countin += 1
else:
    countin = len(snout) / 2 + 1
    while countin < len(snout):
        listb.append(snout[countin])
        countin += 1
if lista == listb:
    print "It's a palindrome!"
else:
    print "It's not a palindrome."
