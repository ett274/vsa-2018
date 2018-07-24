from insertion_bort import *
from quick_sort_of import *
import time
import random

def bubblesort(last):
    n = len(last)
    for i in range(n - 2):
        for j in range(n - 1, i, -1):
            if last[j] < last[j - 1]:
                x = last[j]
                last[j] = last[j - 1]
                last[j - 1] = x
    return last


def timer(funion, test_parameter, amount_of_tries):
    final_time = 0
    for i in range(amount_of_tries):
        tStart = time.clock()
        funion(test_parameter)
        tEnd = time.clock()
        total_time = tEnd - tStart
        final_time += total_time
    return final_time / amount_of_tries


def randlist(x):
    a = []
    for i in range(x):
        a.append(random.randint(1, 100))
    return a


length = int(raw_input("Length of list? "))
tries = int(raw_input("How many checks? "))
lost = randlist(length)

# print "Bubble Sort:", timer(bubblesort, lost, tries) * 1e06
print "Insertion Sort:", timer(is_increasing, lost, tries) * 1e06
print "Quick Sort:", timer(quicksort, lost, tries) * 1e06