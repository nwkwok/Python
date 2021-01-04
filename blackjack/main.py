import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_total = 0
computer_total = 0
is_playing = False


def play_blackjack():
    deal_cards()
    print(f"Dealer's cards: {computer_cards[0], '?'}\n")
    calculate_user_cards(user_total)


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


def calculate_user_cards(total):
    for card in user_cards:
        total += card
    # If user gets blackjack ###########################
    print(f"Your cards are: {user_cards} and your current total is {total}")
    if total == 21:
        print("Blackjack! You win!")
        restart()
    elif total > 21:
        print("Sorry, you bust!")
        restart()
    elif total < 21:
        hit_or_stay()


def hit_or_stay():
    next_step = input("Type 'hit' for another card or type 'stay' to keep your hand: ").lower()
    if next_step == 'hit':
        user_cards.append(pick_random())
        calculate_user_cards(user_total)
    elif next_step == 'stay':
        computer_draw(computer_total, user_total)
    else:
        print("Please type 'hit' or 'stay'")
        hit_or_stay()


def computer_draw(total, user_score):
    print(f"Dealer reveals: {computer_cards}")
    for card in computer_cards:
        total += card
    print(f"Dealer has a total of {total}")
    if total < user_score:
        computer_cards.append(pick_random())
        computer_draw(total)
    elif total == user_score:
        print(f"Looks like it's a draw - Let's try again!")
        deal_cards()
    elif total == 21:
        print(f"Dealer has blackjack! Sorry, you lose!")
    elif total > 21:
        print("Dealer busts. Congrats! You win!")
    elif total > user_score:
        print(f"Dealer has {total} and you have {user_score}. Sorry, you lose!")
        restart()


def hit():
    user_cards.append(pick_random())
    calculate_user_cards(user_total)


start_game = input("Would you like to play a game of blackjack?\n"
                   "Type 'yes' to start or 'no' to exit\n")

if start_game == 'yes':
    is_playing = True
    play_blackjack()

    next_step = input("Type 'hit' for another card or 'stay' to keep your hand: ").lower()
    if next_step == 'hit':
        hit()

    elif next_step == 'stay':
        print('run computer draw function')

elif start_game == 'no':
    is_playing = False
    print('Come back when you\'re ready to play some cards!')
