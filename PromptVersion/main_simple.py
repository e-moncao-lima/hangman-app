## Imports
import random
import hangman_art as art
from wordlists import hangman_wordlist as wl

## defines
#clear = lambda: os.system('cls')
stages = art.stages

## Logo print
print(f'Welcome to the\n{art.logo}', end='\n')

## Choosing word
word_list = wl.word_list
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}')

## Display setup
lives = 6
display = ['_' for c in range(len(chosen_word))]

print(stages[lives])
print(f'{" ".join(display)}', end='\n')

## Displaying
end_of_game = False
guessed = []

while not end_of_game:
    # Gathering guess from the player
    guess = input('Guess a letter: ').lower()
    #clear()

    # Checking if already guessed
    if guess in guessed:
        print(f'Already guessed the letter {guess}\n')
        continue
    else:
        guessed += guess

    # replacing blank with letters if guessed rigth
    for pos in range(len(chosen_word)):
        if chosen_word[pos] == guess:
            display[pos] = guess

    # Discounting lives if guessed wrong
    if chosen_word.find(guess)==-1:
        lives -= 1
        print('Wrong guess!\nLost 1 Life\n')

    # Checking if there is any life still
    if lives <= 0:
        print('You Lost. Ran out of lives.')
        print(stages[lives])
        end_of_game = True        

    print(f'{" ".join(display)}', end='\n')

    if '_' not in display:
        end_of_game = True
        print('You win')

    print(stages[lives])
            


