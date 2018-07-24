def gcf(x, y):
    x_list = []
    y_list = []
    count = 1
    while count <= x:
        if x % count == 0:
            x_list.append(count)
        count += 1
    count = 1
    while count <= y:
        if y % count == 0:
            y_list.append(count)
        count += 1
    common = []
    if len(x_list) > len(y_list):
        for v in x_list:
            if v in y_list:
                common.append(v)
    else:
        for v in y_list:
            if v in x_list:
                common.append(v)
    return common[len(common) - 1]


def lcm(x, y):
    x_multiples = []
    y_multiples = []
    counting = 1
    while counting <= x or counting <= y:
        x_multiples.append(counting * x)
        y_multiples.append(counting * y)
        if x_multiples[counting - 1] in y_multiples:
            return x_multiples[counting - 1]
        elif y_multiples[counting - 1] in x_multiples:
            return y_multiples[counting - 1]
        counting += 1


print "I can take two numbers and give their greatest common factor or their least common multiple!"
first = int(raw_input("What's the first number you want? "))
second = int(raw_input("Second number? "))
question = raw_input("Type 1 to find the greatest common factor, or type 2 to find the least common multiple. ")
if question == "1":
    print "The greatest common factor of " + str(first) + " and " + str(second) + " is " + str(gcf(first, second)) + "."
elif question == "2":
    print "The least common multiple of " + str(first) + " and " + str(second) + " is " + str(lcm(first, second)) + "."
