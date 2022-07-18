# Remember the word Version 2
# Displays 4 words to users. User is prompted to recall one of
# those four words. The user is provided unconditional feedback
# on their response.
# clearing the terminal
import time, os


def main():
    # clear the screen
    os.system('clear')
    # print the header
    print("-" * 80)
    print(" Remember The Word")
    print("-" * 80)

    # read and display the instructions
    file = open("instructions.txt", "r")
    instructions = file.read()
    print(instructions)

    # prompt the user to continue
    input('Press enter key to display the words.')

    # clear the screen
    os.system('clear')
    # print the header
    print("-" * 80)
    print(" Remember The Word")
    print("-" * 80)

    # present words: orange, chair, mouse, sandwich
    # clear the terminal and print the header after each word is printed
    # Replace Adjacent Duplicate Line groups with a for statement
    words = ['orange', 'chair', 'sandwich', 'mouse']
    for word in words:
        print(word)
        time.sleep(2)

        # clear the screen
        os.system('clear')

        # print the header
        print("-" * 80)
        print(" Remember The Word")
        print("-" * 80)

    # prompt user for input
    guess = input('What word begins with the letter c? ')

    # display feedback
    if guess == 'chair':
        print('Congratulations, you are correct.')
    else:
        print('Sorry, you entered ' + guess + '.')
    print('The answer was chair')


main()

