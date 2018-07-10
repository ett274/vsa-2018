# Name: Eliza Thornton and Gator Wallace
# Date: 7/10/18


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""


import random
y = ""
while y != "n":
    choice = raw_input("Do you want to go against the computer or another person? (1 for computer, 2 for person) ")
    if choice == "1":
        x = random.randint(1,9)
        print "Okay, I'm thinking of a number between 1 and 9."
    elif choice == "2":
        while True:
            x = int(raw_input("Okay, player 2 put a number between 1 and 9 here while player 1 looks away. "))
            if 1 <= x <= 9:
                print "CHEATER"
                for p in range(90):
                    print
                break
            else:
                print "That number is invalid."
    player_input = ""
    guesses = 1
    tries = int(raw_input("How many guesses do you think you'll get it in? ")) + 1
    while player_input != str(x) and guesses < tries:
        player_input = raw_input("Guess (or type 'exit' to end): ")
        if player_input == "exit":
            break
        elif int(player_input) < x:
            print "That's too low!"
            guesses += 1
            if tries - guesses == 1:
                print "You have 1 guess left."
            elif guesses == tries:
                break
            else:
                print "You have " + str(tries - guesses) + " guesses left."
        elif int(player_input) > x:
            print "That's too high!"
            guesses += 1
            if tries - guesses == 1:
                print "You have 1 guess left."
            elif guesses == tries:
                break
            else:
                print "You have " + str(tries - guesses) + " guesses left."
        elif int(player_input) == x:
            if guesses == 1:
                print "You got it! You used 1 guess."
            else:
                print "You got it! You used " + str(guesses) + " guesses."
    if guesses == tries:
        print "Out of guesses! You lose :c"
        print "The number was " + str(x) + "!"
    while y != "n" or y != "y":
        y = raw_input("Play again? (y/n): ")
        if y == "y":
            break
        elif y == "n":
            break
        else:
            print "Very funny, do you want to play again or not?"