from data import MENU, resources


def report():
    for r_key in resources.keys():
        if r_key == 'money':
            print(f'{r_key.title()}: ${resources[r_key]:.2f}')
        elif r_key == 'water' or 'milk':
            print(f'{r_key.title()}: {resources[r_key]}ml')
        elif r_key == 'coffee':
            print(f'{r_key.title()}: {resources[r_key]}g')


def update_resources(selection):
    ingredients = MENU[selection]['ingredients']
    ingredient_keys = ingredients.keys()
    for key in ingredient_keys:
        if key == 'water':
            resources['water'] -= ingredients['water']
        if key == 'milk':
            resources['milk'] -= ingredients['milk']
        if key == 'coffee':
            resources['coffee'] -= ingredients['coffee']


def check_coin_type():
    quarter = float(input('How many quarters? '))
    dime = float(input('How many dimes? '))
    nickel = float(input('How many nickels? '))
    penny = float(input('How many pennies? '))
    inserted_coins = [quarter, dime, nickel, penny]
    return inserted_coins


def calculate_inserted_coins(coins_inserted_list):
    quarter = coins_inserted_list[0] * .25
    dime = coins_inserted_list[1] * .10
    nickel = coins_inserted_list[2] * .05
    penny = coins_inserted_list[3] * .01
    return quarter + dime + nickel + penny


def track_money(selection):
    if 'money' not in resources:
        resources['money'] = MENU[selection]['cost']
    else:
        resources['money'] = resources['money'] + MENU[selection]['cost']


def accept_reject_order(selection):
    if amount_inserted >= MENU[selection]['cost']:
        money_returned = amount_inserted - MENU[selection]['cost']
        print(f"Here is your change: ${money_returned:.2f}")
        print(f"Enjoy your {selection} ☕️!")
        return True
    else:
        print(f"Sorry - you don't have enough money! Money returned: ${amount_inserted:.2f}")
        return False


def refill_resources():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 80
    print("Coffee machine has been refilled! Type 'report' to see resource amounts.")


# def check_ingredients(selection):
#     ingredient_cost = MENU[selection]['ingredients']
#     for key in ingredient_cost:
#         if ingredient_cost[key] > resources[key]:
#             print(f'Sorry, there is not enough of {key}. Please type "refill" to refill machine.')
#             return False
#         elif ingredient_cost[key] <= resources[key]:
#             return True


while True:
    coffee_selection = input('What would you like? espresso/latte/cappuccino/report/refill/off?: ').lower()
    if coffee_selection == 'espresso':
        # enough_resources = check_ingredients(coffee_selection)
        # while enough_resources:
        ingredient_cost = MENU['espresso']['ingredients']
        for key in ingredient_cost:
            if ingredient_cost[key] > resources[key]:
                print(f'Sorry, there is not enough of {key}. Please type "refill" to refill machine.')
                enough_resources = False
            elif ingredient_cost[key] <= resources[key]:
                enough_resources = True
        while enough_resources:
            coins_inserted = check_coin_type()
            amount_inserted = calculate_inserted_coins(coins_inserted)
            order_status = accept_reject_order(coffee_selection)
            if order_status:
                track_money(coffee_selection)
                update_resources(coffee_selection)
                enough_resources = False
    if coffee_selection == 'report':
        report()
    if coffee_selection == 'refill':
        refill_resources()
    if coffee_selection == 'off':
        print("Turn me on when you're ready for your caffeine fill!")
        break


# TODO: Turn off coffee machine by entering "off" to the prompt
# TODO: Print Report
# TODO: Check if resources are sufficient
# TODO: Process coins
# TODO: Check if transacation was successful
# TODO: Make Coffee
