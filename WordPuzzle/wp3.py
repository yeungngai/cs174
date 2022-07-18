#
# CMPUT 174
# Lab 2 WordPuzzle version 3
#
# First name: Yi
# Last name: Yang
# Lab section: H04
#
# Description: This the a version 3 word puzzle program
#
#

import os
import random


def display_instructions(filename):
    # INPUT - filename
    # PROCESS - Display the instructions for the game
    # OUTPUT - NONE

    # Display instructions
    file = open(filename, 'r')
    instructions = file.read()
    print(instructions)


def get_guess(num_guesses):
    # INPUT - number of guesses
    # PROCESS - Prompt the user for a guess and indicate the number of guesses remaining
    # OUTPUT - player guess

    # Prompt user to input a letter
    guess = input('Guess a letter (' + num_guesses + ' guesses remaining): ')
    return guess


def update_puzzle_string(puzzle, answer, guess):
    # INPUT - puzzle, answer, guess
    # PROCESS - Given a new guessed letter, updates puzzle
    # OUTPUT - puzzle

    answer_inlist = list(answer)
    if guess in answer_inlist:
        for letter in range(len(answer)):
            if guess == answer_inlist[letter]:
                puzzle[letter * 2] = guess

    return puzzle


def display_puzzle_string(puzzle):
    # INPUT - puzzle
    # PROCESS - Display the current state of the puzzle to the screen (Letters which have been guessed will be revealed).
    # OUTPUT - NONE

    # Display the current state of the puzzle
    print('The answer so far is', ''.join([str(i) for i in puzzle]))


def is_word_found(puzzle):
    # INPUT - puzzle
    # PROCESS - Determines if the player has guessed all the letters in the puzzle or not
    # OUTPUT - found

    found = False
    if '_' not in puzzle:
        found = True

    return found


def display_result(is_win, answer):
    # INPUT - is_win, answer
    # PROCESS - Display whether the player was successful or unsuccessful
    # OUTPUT - NONE

    if is_win:
        print('Good job! You found the word ' + answer + '!')
    else:
        print('Not quite, the correct word was ' + answer + '. ' + 'Better luck next time')


def play_game(puzzle, answer):
    # INPUT - puzzle, answer
    # PROCESS - Prompts the player for guesses and processes them until the player has solved the puzzle or run out of guesses.
    # OUTPUT - is_win

    num_guesses = 4
    is_win = False
    answer_inlist = list(answer)

    while num_guesses != 0:
        pre_puzzle = puzzle
        num_guesses = str(num_guesses)
        guess = get_guess(num_guesses)

        if guess in pre_puzzle:
            num_guesses = int(num_guesses)
            num_guesses = num_guesses - 1
            display_puzzle_string(puzzle)

        if guess in answer_inlist and guess not in puzzle:
            puzzle = update_puzzle_string(puzzle, answer, guess)
            display_puzzle_string(puzzle)

        if guess not in answer_inlist:
            num_guesses = int(num_guesses)
            num_guesses = num_guesses - 1
            display_puzzle_string(puzzle)
        elif is_word_found(puzzle):
            is_win = True
            break

    return is_win


def main():
    os.system('clear')

    # Display instruction
    filename1 = 'instructions.txt'
    display_instructions(filename1)

    # Generate a random word
    list_of_words = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    answer = random.choice(list_of_words)
    puzzle = '_ ' * len(answer)
    puzzle = list(puzzle)

    # Play puzzle
    display_puzzle_string(puzzle)
    is_win = play_game(puzzle, answer)

    # Display result
    display_result(is_win, answer)

    # Prompt user to end the game
    input('Press enter to end the game.')


main()
