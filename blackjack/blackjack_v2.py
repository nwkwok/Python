import random


def validate_answer(question, valid_answers):
    while True:
        answer = input(question).lower()
        if answer in valid_answers:
            return answer


def yes_or_no(question):
    return validate_answer(question + ' Type "y" or "n": ', ['y', 'n'])


while True:
    user_cards = []
    dealer_cards = []
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    start_game = yes_or_no('Would you like to play blackjack?')

    if start_game == 'y':
        for _ in range(2):
            user_cards.append(random.choice(deck))
            dealer_cards.append(random.choice(deck))

    elif start_game == 'n':
        print('Maybe next time!')
        exit()

    print(f"Dealer has {dealer_cards[0], '?'}.\n")
    print(f"You have {user_cards} with a total of {sum(user_cards)}")

    if sum(user_cards) == 21 and len(user_cards) == 2:
        print('You win with a blackjack!')

    while True:
        next_step = validate_answer(
            "Type 'hit' to get another cards or 'stay' to keep your hand as is: ", ['hit', 'stay']
        )

        if next_step == 'hit':
            user_cards.append(random.choice(deck))
            print(f"You have {user_cards} with a total of {sum(user_cards)}")
            if sum(user_cards) == 21 and len(user_cards) == 2:
                print('You win with a blackjack!')
                break
            if 11 in user_cards and sum(user_cards) > 21:
                user_cards.remove(11)
                user_cards.append(1)
                print('Changing 11 --> 1')
                print(f'Your hand is now {user_cards} and your total is {sum(user_cards)}')
            if sum(user_cards) > 21:
                print('Sorry. Looks like you busted!')
                break

        elif next_step == 'stay':
            break

    print(f"Dealer shows {dealer_cards} with a total of {sum(dealer_cards)}")

    while True:
        if sum(dealer_cards) == 21 and len(dealer_cards) == 2:
            print("Dealer wins with a blackjack!")
            break
        elif sum(dealer_cards) < sum(user_cards):
            dealer_cards.append(random.choice(deck))
            print(f"Dealer draws. {dealer_cards} with a total of {sum(dealer_cards)}")
        elif sum(user_cards) < sum(dealer_cards) <= 21:
            # print_scores(dealer)
            print(f'Dealer wins with a total of {sum(dealer_cards)}!')
            break
        elif sum(dealer_cards) > 21:
            # print_scores(dealer)
            print(f'Dealer busts with a total of {sum(dealer_cards)}. You win!')
            break
        elif sum(dealer_cards) == sum(user_cards):
            # print_scores(dealer)
            print(f'Dealer has {sum(dealer_cards)}Looks like it\'s a draw!')
            break

    play_again = yes_or_no("Would you like to play again?")

    if play_again == 'n':
        print('Maybe next time!')
        exit()
