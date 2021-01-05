import random
import os
from art import logo


def set_lives(level):
    if level == 'easy':
        print("Easy livin'! You have 10 attempts remaining to guess the number")
        return 10
    elif level == 'hard':
        print("Looks like you want a mental workout! You have 5 attempts remaining to guess the number")
        return 5
    else:
        print('Please type "easy" or "hard".')


def play():
    print(logo)
    print('Welcome to my Number Guessing Game!')
    print('-----------------------------------')
    start = input("Want to play? Type 'yes' or 'no': ").lower()
    if start == 'yes':
        is_playing = True
        print('-----------------------------------')
    if start == 'no':
        is_playing = False
        print('Maybe next time!')
        exit()
    print('Sweet! I\'m thinking of a number in between 1 and 100. And you\'re gonna guess it.')
    random_number = random.randint(1, 100)
    difficulty = input('Before we start, choose a difficulty. Type "easy" or "hard": ').lower()
    lives = set_lives(difficulty)

    while is_playing:
        guess = int(input("Make a guess: "))
        lives -= 1
        if guess == random_number:
            print("Woo-hoo! You guessed it!")
            is_playing = False
        elif lives == 0:
            is_playing = False
            print(f"Doh! The number was {random_number}")
        elif guess > random_number:
            os.system('clear')
            print(f"You guessed {guess}")
            print("Too high.")
            print("Guess again")
            print(f"You have {lives} attempts remaining")
        else:
            os.system('clear')
            print(f"You guessed {guess}")
            print("Too low.")
            print("Guess again")
            print(f"You have {lives} attempts remaining")

    play_again = input('Want to play again? Type "yes" or "no": ').lower()

    if play_again == 'yes':
        play()
    elif play_again == 'no':
        print("Maybe next time!")
    else:
        print("Please type 'yes' or 'no'")


play()











