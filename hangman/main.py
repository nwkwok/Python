import random
from hangman_art import logo, stages
from hangman_words import word_list
# import os
# from replit import clear

print(logo)
chosen_word = random.choice(word_list)
display = []

for _ in range(len(chosen_word)):
    display += '_'

end_of_game = False
lives = 6
wrong_guess = []

while not end_of_game:
    guess = input('Guess a letter\n').lower()
    print(f'You guessed the letter "{guess}"')
    # os.system('clear')
    # clear()

    if guess in display:
        print('You already guessed this letter. Try a different letter')

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess

    if '_' not in display:
        print('Congraulations! You win!')
        end_of_game = True
    if len(guess) == 0:
        print('To play, you gotta guess a letter... duh!')
    elif len(guess) > 1:
        print('Woah... woah... one letter at a time please!')
    elif guess in wrong_guess:
        print('You already guessed that letter... and it was wrong! Try a different one.')
    elif guess not in chosen_word:
        lives -= 1
        wrong_guess += guess
        if lives == 1:
            print('You have one life left... make it count!')
        elif lives == 0:
            end_of_game = True
            print("You lose!")
        else:
            print(f'You have {lives} lives left')

    print(stages[lives])
    print(display)





