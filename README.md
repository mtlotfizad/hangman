build a simple 'hangman' game that works as follows:
+ Chooses a random word out of 6 words: [hello, marvin, print, filament, order, layer]
+ Display the spaces for the letters of the word (eg: '_ _ _ _ _' for 'order')
+ The user can choose a letter and if that letter exists in the chosen word it should be
shown on the puzzle (eg: asks for 'r' and now it shows '_ r _ _ r' for 'order')
+ The user can only ask 5 letters that don't exist in the word and then it's game overIf the
user wins, congratulate the user and save their high score (you are free to define what is
a “high score”)
Additional requirements:
- Provide a simple API for clients to play the game
- Provide an interface for users to play the game