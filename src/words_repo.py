import random


def get_word_randomly_from_file(word_resource_file_path: str):
    """Retrieve a random word from the file; Tried to use lee memory.
    Actually this method feeds the file content to `get_word_randomly`

   Args:
        word_resource_file_path (str): the path to find the file.

    Returns:
        word: a randomly selected word from the given file
    """
    with(open(word_resource_file_path)) as word_file:
        return get_word_randomly(word_file)


def get_word_randomly(word_iterable):
    """Retrieve a random word from the given iterable; Tried to use lee memory.

   Args:
        word_iterable (iterable): an iterable to a set of words

    Returns:
        word: a randomly selected word from the given file
    """
    word_seen = 0
    selected_word = ""
    for word in word_iterable:
        word = word.strip()
        word_seen += 1
        if random.randrange(1, word_seen + 1) == 1:
            selected_word = word
    return selected_word
