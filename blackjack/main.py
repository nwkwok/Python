import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_total = 0
computer_total = 0
is_playing = False


def pick_random():
    random_card = cards[random.randint(0, (len(cards) - 1))]
    return random_card


def deal_cards():
    while len(user_cards) < 2 and len(computer_cards) < 2:
        user_cards.append(pick_random())
        computer_cards.append(pick_random())


def restart():
    new_game = input("Want to play again? Type 'y' or 'n': ").lower()
    if new_game == 'n':
        print('Thanks for playing!')
        exit()
    elif new_game == 'y':
        play_blackjack()


def calculate_user_cards(user_total):
    for card in user_cards:
        user_total += card
    # If user gets blackjack ###########################
    if user_total == 21:
        print("Blackjack! You win!")
        restart()
    elif user_total > 21:
        print("Sorry, you bust!")
        restart()


def play_blackjack():
    deal_cards()
    calculate_user_cards(user_total)
    print(f"Your cards: {user_cards}\n"
          f"Dealer's cards: {computer_cards[0], '?'}\n")

    next_step = input("Type 'hit' for another card\n "
                      "Type 'stay' to keep your hand: ").lower()

    # If user hits ###########################

    # while user_total < 21
    if next_step == 'hit':
        user_cards.append(pick_random())
        # calculate_user_cards(user_total)
        print(user_cards)

    # If user stays ###########################
    if next_step == 'stay':
        print('stay')


start_game = input("Would you like to play a game of blackjack?\n"
                   "Type 'yes' to start or 'no' to exit\n")

if start_game == 'yes':
    is_playing = True
    play_blackjack()

elif start_game == 'no':
    is_playing = False
    print('Come back when you\'re ready to play some cards!')

