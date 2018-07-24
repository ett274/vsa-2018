# Name: Eliza Thornton
# Date: 7-12-18

# proj05: functions and lists

# Part I

def divisors(num):
    """
    Takes a number and returns all divisors of the number, ordered least to greatest
    :param num: int
    :return: list (int)
    """
    counter = 1
    lst = []
    while counter <= num:
        if num % counter == 0:
            lst.append(counter)
        counter += 1
    s_list = []
    while len(lst) > 0:
        small = min(lst)
        s_list.append(small)
        lst.remove(small)
    # Fill in the function and change the return statment.
    return s_list

def prime(num):
    """
    Takes a number and returns True if the number is prime, otherwise False
    :param num: int
    :return: bool
    """
    count = 2
    while count < num:
        if num % count == 0:
            return False
        else:
            count += 1
    return True
    # Fill in the function and change the return statment.


# Part II:
# REVIEW: Conditionals, for loops, lists, and functions
#
# INSTRUCTIONS:
#
# 1.  Make the string "sentence_string" into a list called "sentence_list" sentence_list
# should be a list of each letter in the string: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'm',
# 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'M', 'o', 'n', 't', 'y', ' ', 'P',
# 'y', 't', 'h', 'o', 'n', '.']
#
# Hint: Use a for loop and with an append function: list.append(letter)
#
sentence_string = "Hello, my name is Monty Python."

sentence_list = []
for mmm in sentence_string:
    sentence_list.append(mmm)
print sentence_list


# 2. Print every item of sentence_list on a separate line using a for loop, like this:
# H
# e
# l
# l
# o
# ,
#
# m
# y
#  .... keeps going on from here.

for mmm in sentence_list:
    print mmm


# 3: Write a for loop that goes through each letter in the list vowels. If the current
# letter is 'b', print out the index of the current letter (should print out the
# number 1).
#
vowels = ['a', 'b', 'i', 'o', 'u', 'y']

counter = 0
for letter in vowels:
    if letter == 'b':
        print vowels[counter]
    counter += 1
# 4: use the index found to change the list vowels so that the b is replaced with an e.
counter = 0
for letter in vowels:
    if letter == 'b':
        vowels[counter] = "e"
    counter += 1


# 5: Loop through each letter in the sentence_string. For each letter, check to see if the
#  number is in the vowels list. If the letter is in the vowels list, add one to a
# counter. Print out the counter at the end of the loop. This counter should show how
# many vowels are in sentence_string.
vowelcount = 0
for letter in sentence_string:
    if letter in vowels:
        vowelcount += 1
print vowelcount

# 6: Make a new function called "vowelFinder" that will return a list of  the vowels
# found in a list (no duplicates).The function's parameters should be "list" and "vowels."


#  Example:
# vowelList = vowelFinder(sentence_list, vowels)
# print vowelList

# ['a', 'e', 'i', 'o', 'y']

def vowelFinder(sentence_list, vowels):
    vowellist = []
    for letter in sentence_list:
        if letter in vowels and letter not in vowellist:
            vowellist.append(letter)
    vowellist.sort()
    return vowellist