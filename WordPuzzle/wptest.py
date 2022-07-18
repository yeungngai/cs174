if guess in answer_inlist:
    puzzle = update_puzzle_string(puzzle, answer, guess)
    display_puzzle_string(puzzle)
else:
    num_guesses = int(num_guesses)
    num_guesses = num_guesses - 1
    display_puzzle_string(puzzle)