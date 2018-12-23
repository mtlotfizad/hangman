import csv
import datetime
import os
from enum import Enum
from string import ascii_lowercase

from words_repo import get_word_randomly_from_file


class GameState(Enum):
    PLAYING = 1
    WIN = 2
    FAIL = 3


class Hangman:

    def __init__(self):
        current_path = os.getcwd().replace("""\\""", "/")
        self.word = get_word_randomly_from_file(current_path + '/resources/words.txt')
        self.censored_index = [False] * len(self.word)
        self.remain_letters = set(ascii_lowercase)
        self.word_found = False
        self.wrong_guess_chars = []
        self.game_state = GameState.PLAYING
        self.number_of_attempts_remained = 5

    def get_display_word(self):
        """Represent the word with censored chars."""
        if len(self.word) != len(self.censored_index):
            raise ValueError('Word length and indices length are not the same')
        displayed_word = ''.join([letter if self.censored_index[i] else '_' for i, letter in enumerate(self.word)])
        return displayed_word

    def get_next_letter(self, next_char) -> bool:
        """Take actions based on guessed character.
            Returns:
                success_status: a boolean which shoes whether the given character was in the word or not
        """
        # you are not allowed to call the method after finishing the game
        if self.game_state != GameState.PLAYING:
            raise ValueError('Game has been already finished with state: {0}'.format(
                'Win' if self.game_state == GameState.WIN else 'Fail'))

        if next_char not in self.remain_letters:
            repeated_word = True
        else:
            repeated_word = False
            self.remain_letters.remove(next_char)

        success_status = True if next_char in self.word else False
        # Which character index should be open?
        for i in range(len(self.word)):
            if self.word[i] == next_char:
                self.censored_index[i] = True
        if not success_status and not repeated_word:
            self.number_of_attempts_remained -= 1
            self.wrong_guess_chars.append(next_char)

        # Check if word is completely solved
        if False not in self.censored_index and len(self.remain_letters) >= 0:
            self.game_state = GameState.WIN
        elif len(self.remain_letters) == 0:
            self.game_state = GameState.FAIL

        return success_status

    def continue_game(self):
        return self.game_state == GameState.PLAYING

    def has_won_game(self):
        return self.game_state == GameState.WIN

    def save_high_score(self, player_name):
        with open('scores.csv', mode='a') as scores_file:
            employee_writer = csv.writer(scores_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            employee_writer.writerow(
                [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), player_name, self.number_of_attempts_remained])
