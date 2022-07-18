# Remember the word Version 3
# Displays 4 words to users. User is prompted to recall one of
# those four words. The user is provided unconditional feedback
# on their response.
# clearing the terminal
# choosing one outcome or the other
# random correct answer every time the game is played
# Words are also different in each play of the game
# Software Quality Requirements - Limiting Literals
import time, os, random


def main():
    continue_game = True
    while continue_game == True:

        # clear the screen
        clear_command = 'clear'
        os.system(clear_command)

        # print the header
        header_border = '-' * 80
        header_content = ' Remember The Word'
        print(header_border)
        print(header_content)
        print(header_border)

        # read and display the instructions
        filename1 = 'instructions.txt'
        mode = 'r'
        file = open(filename1, mode)
        instructions = file.read()
        print(instructions)

        # prompt the user to continue
        input('Press enter key to display the words.')

        # clear the screen
        os.system(clear_command)

        # print the header
        print(header_border)
        print(header_content)
        print(header_border)

        # present words: orange, chair, mouse, sandwich
        # clear the terminal and print the header after each word is printed
        # Replace Adjacent Duplicate Line groups with a for statement
        words_filename = 'words.txt'
        number_of_words = 4
        file = open(words_filename, mode)
        all_words = file.read()
        all_words_list = all_words.splitlines()
        words = random.sample(all_words_list, number_of_words)
        correct_answer = random.choice(words)
        start_letter = correct_answer[0]
        pause_time_in_sec = 2

        for word in words:
            print(word)
            time.sleep(pause_time_in_sec)
            # clear the screen
            os.system(clear_command)
            # print the header
            print(header_border)
            print(header_content)
            print(header_border)

            # prompt user for input
        guess = input('What word begins with the letter ' + start_letter + '? ')

        # display feedback
        if guess == correct_answer:
            print('Congratulations, you are correct.')
        else:  # optional clause of the if statement
            print('Sorry, you entered ' + guess + '.')
        print('The answer was ' + correct_answer + '.')

        response = input('Play again? y/N: ')
        if response.lower() != 'y':
            continue_game = False


main()
