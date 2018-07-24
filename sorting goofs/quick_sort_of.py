import random
def pivot(list, pivot_list):
    if len(list) == 1:
        return list[0]
    else:
        while True:
            pivot = list[random.randint(0, len(list) - 1)]
            if pivot not in pivot_list:
                pivot_list.append(pivot)
                list.remove(pivot)
                less = []
                more = []
                for x in list:
                    if x >= pivot:
                        more.append(x)
                    else:
                        less.append(x)
                return less + [pivot] + more

def quicksort(listy):
    p_list = []
    hammond = pivot(listy, p_list)
    while True:
        hammond = pivot(hammond, p_list)
        if sorted(hammond) == hammond:
            return hammond

randlist = [int(1000*random.random()) for i in xrange(10000)]
print randlist
print quicksort(randlist)