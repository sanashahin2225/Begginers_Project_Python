import random, string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letter) > 0 and lives > 0:
        print('You have used these letters ',''.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('current word ',''.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
            else:
                lives = lives - 1
                print(f'Letter is not in the word. Total life left {lives} ')

        elif user_letter in used_letters:
            print('You have already used that letter. Please try again...')
        
        else:
            print('Invvalid Character')
    
    if lives == 0:
        print(f'Sorry You died, The word was {word}')
    else:
        print(f'You guessed the letter {word}')
hangman()

