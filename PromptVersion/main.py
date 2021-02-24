## Imports
import random
from unidecode import unidecode
import hangman_art as art
import hangman_wordlist2 as wl

class HangmanWorld:
    def __init__(self):
        ## World Setup
        self.stages = art.stages
        self.word_list = wl.word_list
        self.chosen_word = ''
        self.display = '' 
        self.lives = 6
        self.end_of_game = False
        self.guessed = list()

    def new_word(self):
        self.chosen_word = random.choice(self.word_list)
        self.display = ['_' for c in range(len(self.chosen_word))]

    def check_guess(self, guess):
        # Checking if already guessed
        if guess in self.guessed:
            print(f'Already guessed the letter {guess}\n')
            # continue
        else:
            self.guessed += guess

        # replacing blank with letters if guessed right
        for pos in range(len(self.chosen_word)):
            if unidecode(self.chosen_word[pos].lower()) == guess:
                self.display[pos] = self.chosen_word[pos]

        # Discounting lives if guessed wrong
        if (unidecode(self.chosen_word).lower()).find(guess)==-1:
            self.lives -= 1
            print('Wrong guess!\nLost 1 Life\n')

    def check_end(self):
        # Checking if there is any life still
        if self.lives <= 0:
            print('You Lost. Ran out of lives.')
            print(self.stages[self.lives])
            print(f'The word was:\n{self.chosen_word}', end='\n')
            self.end_of_game = True

        if '_' not in self.display:
            self.end_of_game = True
            print(f'{" ".join(self.display)}', end='\n')
            print('Congratulations! You win!')
            

    def display_info(self):
        print(f'Lives remaining: {self.lives}\n')
        print(self.stages[self.lives])
        print(f'{" ".join(self.display)}', end='\n')


def play():    
    ## Logo print
    print(f'Welcome to the\n{art.logo}', end='\n')

    ## Initialize
    world = HangmanWorld()

    ## Choosing word
    world.new_word()
    print(f'Pssst, the solution is {world.chosen_word}')

    ## Play
    while not world.end_of_game:
        # Gathering guess from the player
        world.display_info()
        guess = input('Guess a letter: ').lower()
        world.check_guess(guess)
        world.check_end()            

if __name__ == '__main__':
    play()