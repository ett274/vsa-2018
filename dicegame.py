import random


def display_scores(one, two):
    if one == 1 and two == 1:
        print "Player 1 has 1 point, and Player 2 has 1 point."
    elif two == 1:
        print "Player 1 has " + str(one) + " points, and Player 2 has 1 point."
    elif one == 1:
        print "Player 1 has 1 point, and Player 2 has " + str(two) + " points."
    else:
        print "Player 1 has " + str(one) + " points, and Player 2 has " + str(two) + " points."


play1_points = 0
play2_points = 0
play1_wager = 1
play2_wager = 1
play_again = ""
# while True:
#     play_again = raw_input("How many times do you want to play? ")
#     try:
#         val = int(play_again)
#     except ValueError:
#         print "That's not a number!"
#     else:
#         break
# play_again = int(play_again)
# for y in range(play_again):
#     x = random.randint(1, 6)
#     print x
#     print
#     if x % 2 == 0:
#         print "Player 2 gets 1 point!"
#         play2_points += 1
#     else:
#         print "Player 1 gets 1 point!"
#         play1_points += 1
#     print display_scores(play1_points, play2_points)
#     print

while play_again != "YOTE":
    x = random.randint(1, 6)
    print x
    print
    if x % 2 == 0:
        play2_points += play2_wager
        if play2_wager == 1:
            print "Player 2 gets 1 point!"
        else:
            print "Player 2 gets " + str(play2_wager) + " points!"
        play1_wager = 1
    else:
        play1_points += play1_wager
        if play1_wager == 1:
            print "Player 1 gets 1 point!"
        else:
            print "Player 1 gets " + str(play1_wager) + " points!"
        play2_wager = 1
    display_scores(play1_points, play2_points)
    while True:
        play_again = raw_input("Play again? (y/n) ").lower()
        if play_again == "y":
            break
        elif play_again == "n":
            play_again = "YOTE"
            break
        else:
            print "Sorry, I don't understand that."
    if play_again == "y":
        while True:
            play1_choice = raw_input("Player 1, do you want to bet half of your points? (y/n) ").lower()
            if play1_choice == "y":
                play1_wager = play1_points
                play1_points = play1_points / 2
                break
            elif play1_choice == "n":
                break
            else:
                print "Sorry, I don't understand that."
        while True:
            play2_choice = raw_input("Player 2, do you want to bet half of your points? (y/n) ").lower()
            if play2_choice == "y":
                play2_wager = play2_points
                play2_points = play2_points / 2
                break
            elif play2_choice == "n":
                break
            else:
                print "Sorry, I don't understand that."