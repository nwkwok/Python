## This version of blackjack runs great but I'm struggling to restart the script once it is complete

import random
from art import logo

print(logo)
user_cards = []
dealer_cards = []
is_playing = False
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    """"Inputs two random cards into user_cards and dealer_cards"""
    for _ in range(2):
        user_cards.append(random.choice(deck))
        dealer_cards.append(random.choice(deck))


def deal_random_card(player):
    """draws random card for the player specified in the parameter"""
    return player.append(random.choice(deck))


def blackjack():
    """Initializes an input to allow user to start a game of blackjack"""
    start_game = input('Would you like to play blackjack? Type "y" or "n": ').lower()
    if start_game == 'y':
        deal_cards()
    elif start_game == 'n':
        print('Maybe next time!')
        exit()
    else:
        print('Invalid selection. Please try again')
        blackjack()


def calculate_cards(cards):
    """Takes a list of cards and calculates the total"""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        print('Changing 11 --> 1')
        print(f'Your hand is now {cards} and your total is {sum(cards)}')
    elif sum(cards) > 21:
        print('Sorry. Looks like you busted!')
        restart_game()
    elif sum(cards) == 21 and len(cards) == 2:
        print('You win with a blackjack!')
        restart_game()


def hit(player):
    """Gives random card to player when they type 'hit'"""
    deal_random_card(player)


def restart_game():
    """Reset variables and restart game"""
    global is_playing, user_cards, dealer_cards
    play_again = input("Want to play again? Type 'y' for another game or 'n' to stop.").lower()
    if play_again == 'y':
        print('Why won\'t my game restart!?')
    elif play_again == 'n':
        print('Maybe next time!')
        exit()
    elif play_again != 'y' or play_again != 'n':
        print('Please type "y" or "n".')
        restart_game()


def compare_scores(player, dealer):
    """Begin score comparisons if user stays as dealer takes their turns"""
    def print_scores(computer):
        """Prints score computer"""
        print(f"Dealer shows {computer} with a total of {sum(computer)}")

    if sum(dealer) == 21 and len(dealer) == 2:
        print("Dealer wins with a blackjack!")
        restart_game()
    elif sum(dealer) < sum(player):
        print_scores(dealer)
        deal_random_card(dealer)
        print(f"Dealer draws. {dealer}")
        compare_scores(player, dealer)
    elif sum(player) < sum(dealer) <= 21:
        print_scores(dealer)
        print('Dealer wins!')
        restart_game()
    elif sum(dealer) > 21:
        print_scores(dealer)
        print('Dealer busts. You win!')
        restart_game()
    elif sum(dealer) == sum(player):
        print_scores(dealer)
        print('Looks like it\'s a draw!')
        restart_game()


blackjack()
is_playing = True

print(f"Dealer has {dealer_cards[0], '?'}.\n")
print(f"You have {user_cards} with a total of {sum(user_cards)}")
calculate_cards(user_cards)

while is_playing:
    next_step = input("Type 'hit' to get another cards or 'stay' to keep your hand as is: ").lower()
    if next_step == 'hit':
        hit(user_cards)
        print(f"You have {user_cards} with a total of {sum(user_cards)}")
        calculate_cards(user_cards)
    elif next_step == 'stay':
        compare_scores(user_cards, dealer_cards)
    else:
        print('Oops! Try again.')

restart_game()


# First Attempt ###########
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user_cards = []
# computer_cards = []
# user_total = 0
# computer_total = 0
# is_playing = False
#
#
# def play_blackjack():
#     deal_cards()
#     print(f"Dealer's cards: {computer_cards[0], '?'}\n")
#     calculate_user_cards(user_total)
#
#
# def pick_random():
#     random_card = cards[random.randint(0, (len(cards) - 1))]
#     return random_card
#
#
# def deal_cards():
#     while len(user_cards) < 2 and len(computer_cards) < 2:
#         user_cards.append(pick_random())
#         computer_cards.append(pick_random())
#
#
# def restart():
#     new_game = input("Want to play again? Type 'y' or 'n': ").lower()
#     if new_game == 'n':
#         print('Thanks for playing!')
#         exit()
#     elif new_game == 'y':
#         play_blackjack()
#
#
# def calculate_user_cards(total):
#     for card in user_cards:
#         total += card
#     # If user gets blackjack ###########################
#     print(f"Your cards are: {user_cards} and your current total is {total}")
#     if total == 21:
#         print("Blackjack! You win!")
#         restart()
#     elif total > 21:
#         print("Sorry, you bust!")
#         restart()
#     elif total < 21:
#         hit_or_stay()
#
#
# def hit_or_stay():
#     next_step = input("Type 'hit' for another card or type 'stay' to keep your hand: ").lower()
#     if next_step == 'hit':
#         user_cards.append(pick_random())
#         calculate_user_cards(user_total)
#     elif next_step == 'stay':
#         computer_draw(computer_total, user_total)
#     else:
#         print("Please type 'hit' or 'stay'")
#         hit_or_stay()
#
#
# def computer_draw(total, user_score):
#     print(f"Dealer reveals: {computer_cards}")
#     for card in computer_cards:
#         total += card
#     print(f"Dealer has a total of {total}")
#     if total < user_score:
#         computer_cards.append(pick_random())
#         computer_draw(total)
#     elif total == user_score:
#         print(f"Looks like it's a draw - Let's try again!")
#         deal_cards()
#     elif total == 21:
#         print(f"Dealer has blackjack! Sorry, you lose!")
#     elif total > 21:
#         print("Dealer busts. Congrats! You win!")
#     elif total > user_score:
#         print(f"Dealer has {total} and you have {user_score}. Sorry, you lose!")
#         restart()
#
#
# def hit():
#     user_cards.append(pick_random())
#     calculate_user_cards(user_total)
#
#
# start_game = input("Would you like to play a game of blackjack?\n"
#                    "Type 'yes' to start or 'no' to exit\n")
#
# if start_game == 'yes':
#     is_playing = True
#     play_blackjack()
#
#     next_step = input("Type 'hit' for another card or 'stay' to keep your hand: ").lower()
#     if next_step == 'hit':
#         hit()
#
#     elif next_step == 'stay':
#         print('run computer draw function')
#
# elif start_game == 'no':
#     is_playing = False
#     print('Come back when you\'re ready to play some cards!')