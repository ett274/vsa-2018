import random

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
   return alist

def random_list(n, low, upp):
    list = []
    for x in range(n):
        list.append(random.randint(low, upp))
    return list


lost = random_list(100, 1, 100)
print lost
print selectionSort(lost)