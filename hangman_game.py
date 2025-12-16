import random
import string

def get_word(word_list):
    return random.choice(word_list)

def display_hangman(tries):
    stages = [
        '''
        ------
        |    |
        |
        |
        |
        |
        =========''',
        '''
        ------
        |    |
        |    O
        |
        |
        |
        =========''',
        '''
        ------
        |    |
        |    O
        |    |
        |
        |
        =========''',
        '''
        ------
        |    |
        |    O
        |   /|
        |
        |
        =========''',
        '''
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        =========''',
        '''
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |
        =========''',
        '''
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |   /
        =========''',
        '''
        ------
        |    |
        |    O
        |   /|\\
        |    |
        |   / \\
        ========='''
    ]
    return stages[tries]

def play_hangman():
    word_list = ["PYTHON", "HANGMAN", "GUESS", "CODE"]
    word = get_word(word_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(display_hangman(6 - lives))
        print('Used letters:', ' '.join(used_letters))
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print('Current word:', ' '.join(word_display))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word.')
        elif user_letter in used_letters:
            print('You already guessed that letter.')
        else:
            print('Invalid character.')

    if lives == 0:
        print(display_hangman(6))
        print('You died. The word was:', word)
    else:
        print('You guessed the word! 🎉')

# Start the game
play_hangman()
