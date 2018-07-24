import random
play1_points = 0
play2_points = 0
while True:
    x = random.randint(1,6)
    print x
    if x % 2 == 0:
        print "Player 2 gets 1 point!"
        play2_points += 1
    else:
        print "Player 1 gets 1 point!"
        play1_points += 1
    if play1_points == 1 and play2_points == 1:
        print "Player 1 has 1 point, and Player 2 has 1 point."
    elif play2_points == 1:
        "Player 1 has " + str(play1_points) + " points, and Player 2 has 1 point."
    elif play1_points -- 1:
        "Player 1 has 1 point"