import unittest

from words_repo import get_word_randomly_from_file, get_word_randomly


class TestWordsRepo(unittest.TestCase):

    def test_broken_file_as_input(self):
        with self.assertRaises(FileNotFoundError):
            get_word_randomly_from_file('invalid_path')

        self.assertRaises(TypeError, get_word_randomly_from_file, None)

    def test_sample_file_as_input(self):
        word = get_word_randomly_from_file('resources/words.txt')
        self.assertIn(word, ['hello', 'world', 'python'], 'Returned word nof found in the list')

    def test_sample_array_as_input(self):
        word_list = ['hello', 'world', 'python']
        word = get_word_randomly(word_list)
        self.assertIn(word, word_list, 'Returned word nof found in the list')


if __name__ == '__main__':
    unittest.main()
