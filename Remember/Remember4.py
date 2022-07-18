# Remember the word Version 4
# Version 4
#  - Program can repeat or restart if player enter y or Y
#  - Non Adjacent duplicate line groups - user defined function
import os
import random
import time


def display_header():
    # INPUT
    # PROCESS - clear the terminal and display the header
    # OUTPUT - NONE

    # clear the screen
    clear_command = 'clear'
    os.system(clear_command)

    # print the header
    header_border = '-' * 80
    header_content = ' Remember The Word'
    print(header_border)
    print(header_content)
    print(header_border)
    # return None or return will also work
    return


def display_instructions(filename):
    # INPUT parameter - filename
    # Process displays the instructions
    # OUTPUT None

    # read and display the instructions
    # filename1 = 'instructions.txt'
    mode = 'r'
    file = open(filename, mode)
    instructions = file.read()
    print(instructions)


def sample_words(filename):
    # INPUT - parameter filename - name of the file with all the words
    # PROCESS sample 4 random words
    # OUTPUT - return a list of words

    number_of_words = 4
    mode = 'r'
    file = open(filename, mode)
    all_words = file.read()
    all_words_list = all_words.splitlines()
    words = random.sample(all_words_list, number_of_words)

    return words  # throw


def display_words(words):
    # INPUT - parameter - words
    # PROCESS - display the words in list
    # OUTPUT - return value-None

    pause_time_in_sec = 0.5
    for word in words:
        print(word)
        time.sleep(pause_time_in_sec)
        display_header()


def get_guess(start_letter):
    # INPUT - parameter - start letter
    # PROCESS - prompt the player with the question
    # OUTPUT - return is the string entered by the player - game

    guess = input('What word begin with the letter ', start_letter)

    return guess


def display_feedback(guess, correct_answer):
    # INPUT - parameter guess, correct answer
    # PROCESS - display the outcome
    # OUTPUT

    if guess == correct_answer:
        print('Congratulations, you are correct.')

    else:  # optional clause of the if statement
        print('Sorry, you entered ' + guess + '.')
    print('The answer was ' + correct_answer + '.')


def play_again():
    # INPUT
    # PROCESS
    # OUTPUT -- continue game

    continue_game = True
    response = input('Play again? y/N ')
    if response.upper() != 'Y':
        continue_game = False

    return continue_game


def main():
    continue_game = True
    while continue_game:
        display_header()

        # read and display the instructions
        filename1 = input('Enter filename >')
        display_instructions(filename1)  # argument of the function

        # prompt the user to continue
        input('Press enter key to display the words.')

        display_header()

        # present words: orange, chair, mouse, sandwich
        # clear the terminal and print the header after each word is printed
        # Replace Adjacent Duplicate Line groups with a for statement
        words_filename = 'words.txt'
        words = sample_words(words_filename)  # argument is words.txt

        correct_answer = random.choice(words)
        start_letter = correct_answer[0]

        # Display words
        display_words(words)

        # prompt user to input
        guess = get_guess(start_letter)

        # Display feedback
        display_feedback(guess, correct_answer)

        # play again ?
        continue_game = play_again()


main()
