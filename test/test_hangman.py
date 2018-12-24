import unittest

from hangman import Hangman


class TestHangman(unittest.TestCase):

    def test_display_word(self):
        hangman = Hangman()
        display_word = hangman.get_display_word()
        word_len = len(hangman._word)
        self.assertEqual(display_word, '_' * word_len)

    def test_successful_letter(self):
        hangman = Hangman()
        guess_status = hangman.get_next_letter(hangman._word[0])
        self.assertEqual(guess_status, True)


if __name__ == '__main__':
    unittest.main()
