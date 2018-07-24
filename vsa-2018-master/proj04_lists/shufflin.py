import random


def shuffle(x):
    new_list = []
    while len(x) > 0:
        yum = x[random.randint(0, len(x) - 1)]
        new_list.append(yum)
        x.remove(yum)
    return new_list


def roundabout(x):
    counter = 1
    while True:
        davey = shuffle(x)
        print " ".join(davey)
        if davey == x:
            break
        else:
            counter += 1
    if counter == 1:
        print "Wow, this only took one try. Look at you."
    else:
        print "This took " + str(counter) + " tries."


def deal(deq, ham, num):
    for x in range(num):
        ham.append(deq[x])
        deq.remove(deq[x])
    return ham


deck = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AD", "2D", "3D", "4D", "5D",
        "6D," "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AC", "2C", "3C", "4C", "5C", "6C," "7C", "8C", "9C", "10C",
        "JC", "QC", "KC", "AS", "2S", "3S", "4S", "5S", "6S," "7S", "8S", "9S", "10S", "JS", "QS", "KS"]

deck = shuffle(deck)
hand = []
number = int(raw_input("How many cards? "))

print deal(deck, hand, number)
