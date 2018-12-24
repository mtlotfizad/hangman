from string import ascii_lowercase

from readchar import readchar

from hangman import Hangman


def get_next_letter():
    char_read = False
    while not char_read:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single character'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        else:
            char_read = True
    return next_letter


if __name__ == '__main__':
    hangman = Hangman()
    print('I have a word for you, can you guess what is it? ')

    while hangman.continue_game():
        print('The closure part of the word {0} '.format(hangman.get_display_word()))
        print('You have {0} guesses'.format(hangman._number_of_attempts_remained))
        print('Previous unsuccessful guesses: {0}'.format(' '.join(hangman._wrong_guess_chars)))
        print('Please give me your next guess:')
        next_letter = get_next_letter()
        status = hangman.get_next_letter(next_letter)
        if status:
            print('{0} is in the word!'.format(next_letter))
        else:
            print('{0} is NOT in the word!'.format(next_letter))

    if hangman.has_won_game():
        print('Hooray! you won the game.')
        player_name = input('Please give me your name to add to high score table:')
        hangman.save_high_score(player_name)
    else:
        print('Sorry, you failed. Don\'t worry you can beat it next time ;)')
