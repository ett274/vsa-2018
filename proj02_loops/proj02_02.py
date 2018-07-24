# Name: Eliza Thornton
# Date: 7-10-18

# proj02_02: Fibonacci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

x = int(raw_input("How many Fibonacci numbers do you want to generate? "))
if x <= 0:
    print "Okay, fine then, smart alec."
elif x == 1:
    lister = [1]
    print lister
else:
    lister = [1, 1]
    count = 1
    while count < x - 1:
        lister.append(lister[count] + lister[count - 1])
        count += 1
    else:
        print lister

dos = int(raw_input("How many powers of 2 do you want to see? "))
listerine = []
if dos <= 0:
    print "Okay, fine then, smart alec."
else:
    count = 1
    while count <= dos:
        listerine.append(2**count)
        count += 1
    print listerine

mmm = int(raw_input("Give me a number and I'll tell you all its divisors: "))
blister = []
if mmm <= 0:
    print "Sorry! I can only do whole numbers."
else:
    cont = 1
    while cont <= mmm:
        if mmm % cont == 0:
            blister.append(cont)
        cont += 1
    print blister
