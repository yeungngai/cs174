#
# CMPUT 174
# Lab 2 WordPuzzle version 2
#
# First name: Yi
# Last name: Yang
# Lab section: H04
#
# Description: This the a version 2 word puzzle program
#
#
import os
import random


def main():
    #os.system('clear')

    # Display instructions
    file = open('instructions.txt', 'r')
    instructions = file.read()
    print(instructions)

    # Generate a random word
    list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    answer = random.choice(list_of_words)
    answer_inlist = list(answer)

    # Prompt user to input a letter
    answer_underscore = '_ ' * len(answer)
    print('The answer so far is', answer_underscore)
    user_input = input('Guess a letter: ')

    # Determine whether user input is correct or not and display messages
    if user_input not in answer_inlist:
        print('The answer so far is', answer_underscore)
        print('Not quite, the correct word was ' + answer + '. ' + 'Better luck next time')

    else:
        answer_underscore = list(answer_underscore)
        for letter in range(len(answer)):
            if user_input == answer_inlist[letter]:
                answer_underscore[letter*2] = user_input
        print('The answer so far is', ''.join(str(i) for i in answer_underscore))
        print('Good job! You found the word ' + answer + '!')

    # Prompt user to end the game
    input('Press enter to end the game.')


main()
