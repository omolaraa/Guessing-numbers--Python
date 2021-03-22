from random import randint


def play():
    print('Guess between 1 and 5.')
    chances = 3
    guesses_left = 3
    players_guesses = 0
    guess = ''
    right_guess = randint(1, 5)
    while guesses_left > 0:
        guess = input('What number am I guessing? \n')
        guess = int(guess)
        players_guesses += 1
        guesses_left -= 1
        if guess < right_guess:
            print('Your guess is too low')
        elif guess > right_guess:
            print('Your guess is too high')
        else:
            print(f'You are right!')
            print(f'Total attempts used: {players_guesses} out of {chances}')
            break
    if guesses_left == 0 and guess != right_guess:
        print(f'The answer is {right_guess}')


def continue_game():
    play_again = input('Do you want to play again? Y/N \n').upper()
    if play_again == 'N':
        print('Thanks for playing.')
    elif play_again == 'Y':
        play()
    else:
        print('Invalid input!')


play()
continue_game()