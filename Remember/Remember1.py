# Remember The Word Version 1 - this version display, prompt and wait
# Name
# Lab Section
import time


def main():
    # display the header
    print('-' * 80)
    print('Remember The Word')
    print('-' * 80)

    # display instruction
    file = open('instructions.txt', 'r')
    instructions = file.read()
    print(instructions)

    # Prompt the player to press enter
    input('Press enter key to display the words')

    # display the words
    print('oranges')
    time.sleep(2)
    print('chair')
    time.sleep(2)
    print('sandwich')
    time.sleep(2)
    print('mouse')
    time.sleep(2)

    # Prompt the player to enter word
    guess = input('What word begins with the letter c? ')

    # display feedback
    print('Congratulations, you are correct')
    print('Sorry you entered ' + guess)
    print('The answer was chair')


main()
