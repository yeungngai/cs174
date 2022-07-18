#
# Cmput 174
# Lab 1 Guess The Number
#
# First name: Yi
# Last name: Yang
# Lab section: H04
#
# Description: This program will randomly generate a number and prompt user to guess the number.
#
#
#


def main():

    import time
    import random

    # get player name
    name = input('What is your name? ')

    # Generate a random number between 1 and 10
    number = random.randint(1, 10)

    # Display instruction
    print('I am think of a number between 1 and 10.')

    # wait
    print('Pausing...')
    time.sleep(1.5)

    # Prompt user to enter a number
    guess = input('What is the number? ')

    # Display results
    print('the number was', number, '.')
    print('You guessed ', guess, '.')

    # say goodbye by name
    print('Goodbye for now ' + name)


main()
