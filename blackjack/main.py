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
        user_cards = []
        dealer_cards = []
        is_playing = False
        blackjack()
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