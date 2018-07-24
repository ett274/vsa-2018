import time
import random

list_len = 1000
lst = []
total_total_time = 0

x = 1000
tatol = 0
while x > 0:
    tatol += x
    x -= 1
print tatol * 100 * 1000

for i in range (100):
    tStart = time.clock()
    for num in range(list_len):
        lst.append(random.randint(0, 100))
    s_list = []
    while len(lst) > 0:
        small = min(lst)
        s_list.append(small)
        lst.remove(small)
    tEnd = time.clock()
    total_time = tEnd - tStart
    total_total_time += total_time

print s_list
print "time =", total_total_time / 100
