import random
print "Let's play rock, paper, scissors!"
play_again = ""
def tie(poot_wager):
    print "Tie! Let's try again!"
    poot_wager = poot_wager * 2
    print "(The point wager just went up to " + str(poot_wager) + "!)"
    return poot_wager

player_points = 0
cpu_points = 0
while play_again != "exit":
    finish = 0
    point_wager = 1
    while finish == 0:
        player_input = raw_input("Type in your choice: ")
        player_input = player_input.lower()
        cpu_input = random.randint(1,3)
# 1 for rock, 2 for paper, 3 for scissors
        if player_input == "rock" and cpu_input == 1:
            point_wager = tie(point_wager)
        elif player_input == "rock" and cpu_input == 2:
            print "Paper beats rock! I win!"
            cpu_points += point_wager
            if point_wager == 1:
                print "I got 1 point!"
            else:
                print "I got " + str(point_wager) + " points!"
            break
        elif player_input == "rock" and cpu_input == 3:
            print "Rock beats scissors! You win!"
            player_points += point_wager
            if point_wager == 1:
                print "You got 1 point!"
            else:
                print "You got " + str(point_wager) + " points!"
            break
        elif player_input == "paper" and cpu_input == 1:
            print "Paper beats rock! You win!"
            player_points += point_wager
            if point_wager == 1:
                print "You got 1 point!"
            else:
                print "You got " + str(point_wager) + " points!"
            break
        elif player_input == "paper" and cpu_input == 2:
            point_wager = tie(point_wager)
        elif player_input == "paper" and cpu_input == 3:
            print "Scissors beats paper! I win!"
            cpu_points += point_wager
            if point_wager == 1:
                print "I got 1 point!"
            else:
                print "I got " + str(point_wager) + " points!"
            break
        elif player_input == "scissors" and cpu_input == 1:
            print "Rock beats scissors! I win!"
            cpu_points += point_wager
            if point_wager == 1:
                print "I got 1 point!"
            else:
                print "I got " + str(point_wager) + " points!"
            break
        elif player_input == "scissors" and cpu_input == 2:
            print "Scissors beats paper! You win!"
            player_points += point_wager
            if point_wager == 1:
                print "You got 1 point!"
            else:
                print "You got " + str(point_wager) + " points!"
            break
        elif player_input == "scissors" and cpu_input == 3:
            point_wager = tie(point_wager)
            break
        else:
            print "Invalid input!"
    point_wager = 1
    finish = 1
    if player_points == 1 and cpu_points == 1:
        print "You have 1 point, and I have 1 point."
    elif player_points == 1:
        print "You have 1 point, and I have " + str(cpu_points) + " points."
    elif cpu_points == 1:
        print "You have " + str(player_points) + " points, and I have 1 point."
    else:
        print "You have " + str(player_points) + " points, and I have " + str(cpu_points) + " points."
    play_again = raw_input("Type exit to quit, or press enter to continue! ")