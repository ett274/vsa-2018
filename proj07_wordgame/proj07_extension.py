# Name: Eliza Thornton
# Date: 7-16-18

# proj07 Extension

from proj07 import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, 
	and return it. This word should be calculated by considering all possible 
	permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    x = '.'
    greatest_score = 0
    y = calculate_handlen(hand)
    for n in range(y + 1):
        p_list = get_perms(hand, n)
        for item in p_list:
            if is_valid_word(item, hand, word_list) is True:
                if greatest_score < get_word_score(item, y):
                    greatest_score = get_word_score(item, y)
                    x = item
    return x
#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices 
        (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    total = 0
    while True:
        display_hand(hand)
        print "Calculating..."
        word = comp_choose_word(hand, word_list)
        print "Time:", totalTime
        if word == ".":
            break
        hand = update_hand(hand, word)
        total += get_word_score(word, calculate_handlen(hand))
        print "Score for " + word + " earns " + str(get_word_score(word, calculate_handlen(hand)))
        print "Total computer score is " + str(total) + "."
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand 
        (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    p_hand = deal_hand(HAND_SIZE)
    x = p_hand.copy()
    while True:
        choice = raw_input("Input a 'u' to play the game yourself, or input a 'c' to let a computer do it: ").lower()
        if choice == 'u':
            play_hand(p_hand, word_list)
        elif choice == 'c':
            comp_play_hand(p_hand, word_list)
        while True:
            input = raw_input("Input 'n' to play a new hand, 'r' to play the last hand again, or 'q' to quit: ").lower()
            if input == 'n' or input == 'r' or input == 'e':
                break
            else:
                print "Invalid input."
        if input == 'n':
            p_hand = deal_hand(HAND_SIZE)
            x = p_hand.copy()
        elif input == 'q':
            print "Thanks for playing!"
            break
        elif input == 'r':
            print "Playing with the previous hand..."
            p_hand = x
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

# testnum = int(raw_input("How many times do you want to test this? "))
# totaltotaltime =
# for x in range(testnum):
#     deal = deal_hand(HAND_SIZE)
#     tStart = time.clock()
#     comp_choose_word(deal, word_list)
#     tEnd = time.clock()
#     totaltime = tEnd - tStart
#     totaltotaltime