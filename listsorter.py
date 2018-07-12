o_list = [7, 11, 5, 19, 1]
s_list = []
while len(o_list) > 0:
    small = o_list[0]
    number = 0
    count = 0
    for x in o_list:
        if x < small:
            small = x
            number = count
        count += 1
    s_list.append(small)
    o_list.remove(o_list[number])
print s_list
