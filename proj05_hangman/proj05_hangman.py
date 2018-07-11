# Name: Eliza, Elizabeth, Maddie
# Date: 7-11-18


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
while True:
    word = choose_word(wordlist)
    letters = []
    for x in word:
        letters.append(x)
    blanks = []
    for x in word:
        blanks.append("_")
    player_letters = []

    for letter in string.lowercase:
        player_letters.append(letter)
    print "I'm thinking of a word that is " + str(len(word)) + " letters long."
    guesses = len(word) + 3
    while letters != blanks and guesses > 0:
        print " ".join(blanks)
        print "Available letters: " + "".join(player_letters)
        if guesses == 1:
            print "You have 1 guess left."
        else:
            print "You have " + str(guesses) + " guesses left."
        player_input = raw_input("Guess a letter: ")
        if player_input not in string.lowercase and player_input != word:
            print "Invalid input."
        elif player_input == word:
            break
        elif player_input in letters and player_input in player_letters:
            counter = 0
            for let in word:
                if player_input == let:
                    blanks[counter] = player_input
                counter += 1
            player_letters.remove(player_input)
            if letters != blanks:
                print "Great guess!"
        elif player_input not in player_letters:
            print "You already guessed that!"
        else:
            print "Try again."
            guesses -= 1
            player_letters.remove(player_input)
        print
    if guesses == 0:
        print "You lost! The word was " + word + "."
    else:
        print word
        print
        print "Great job! You won!"
    yn = raw_input("Type 'quit' to quit, or press enter to play again! ")
    if yn == "quit":
        break
    else:
        print
        print
print "Okay bye!"