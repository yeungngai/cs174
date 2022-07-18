#
# CMPUT 174
# Lab 2 WordPuzzle version 1
#
# First name: Yi
# Last name: Yang
# Lab section: H04
#
# Description: This the a version 1 word puzzle program
#
#
import random, os


def main():
    os.system('clear')

    # Display instructions
    file = open('instructions.txt', 'r')
    instructions = file.read()
    print(instructions)

    # Generate a random word
    list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    answer = random.choice(list_of_words)

    # Prompt user to enter a letter
    word = answer.replace(answer[0], '_', 1)
    print('The answer so far is', word)
    user_input = input('Guess a letter: ')

    # Determine whether or not user input is correct and display messages
    if user_input != answer[0]:
        print('Not quite, the correct word was ' + answer + '. ' + 'Better luck next time')

    else:
        print('Good job! You found the word ' + answer + '!')

    # Prompt user to end the game
    input('Press enter to end the game.')


main()
