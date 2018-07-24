import random

def is_increasing(loast):
    for j in range(len(loast)):
        i = j - 1
        while loast[i] > loast[j] and j > 0:
            a = loast[i]
            loast[i] = loast[j]
            loast[j] = a
            i -= 1
            j -= 1
    return loast


def is_decreasing(loast):
    for j in range(len(loast)):
        i = j - 1
        while loast[i] < loast[j] and j > 0:
            a = loast[i]
            loast[i] = loast[j]
            loast[j] = a
            i -= 1
            j -= 1
    return loast


def searchin(list, value):
    if value not in list:
        return "null"
    else:
        for x in range(0, len(list)):
            if list[x] == value:
                return x

def bi_searchin(list, value):
    if value not in list:
        return 'null'
    else:
        upp = len(list)
        low = 0
        while True:
            x = (upp/low)/2
            if list[x] == value:
                return x
            elif list[x] < value:
                upp = upp / 2
            elif list[x] > value:
                low = x

# B = [1, 15, 29, 34, 44, 51, 66, 69, 71, 77, 79, 91]
# print is_increasing(B)
# print searchin(is_increasing(B), 69)
