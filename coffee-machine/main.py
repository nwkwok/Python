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
    for key in ingredients.keys():
        resources[key] -= ingredients[key]


def coin_inputs():
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


def refill_resources():
    resources['water'] = 300
    resources['milk'] = 200
    resources['coffee'] = 80
    print("Coffee machine has been refilled! Type 'report' to see resource amounts.")


def check_ingredients(selection):
    ingredient_cost_list = MENU[selection]['ingredients']
    for c_key in ingredient_cost_list:
        if ingredient_cost_list[c_key] > resources[c_key]:
            print(f'Sorry, there is not enough of {c_key}. Please type "refill" to refill machine.')
            return False
    return True


def accept_reject_order(selection, total_amount):
    if total_amount >= MENU[selection]['cost']:
        money_returned = total_amount - MENU[selection]['cost']
        print(f"Here is your change: ${money_returned:.2f}")
        print(f"Enjoy your {selection} ☕️!")
        return True
    print(f"Sorry - you don't have enough money! Money returned: ${total_amount:.2f}")
    return False


def run_coffee_order(selection):
    enough_resources = check_ingredients(selection)
    if enough_resources == False:
        return False
    coins_inserted = coin_inputs()
    amount_inserted = calculate_inserted_coins(coins_inserted)
    order_status = accept_reject_order(selection, amount_inserted)
    if order_status:
        track_money(selection)
        update_resources(selection)
    return False


def run_coffee_cycle():
    coffee_selection = input('What would you like? espresso/latte/cappuccino/report/refill/off?: ').lower()
    if coffee_selection in {'espresso', 'latte', 'cappuccino'}:
        run_coffee_order(coffee_selection)
    elif coffee_selection == 'report':
        report()
    elif coffee_selection == 'refill':
        refill_resources()
    elif coffee_selection == 'off':
        print("Turn me on when you're ready for your caffeine fill!")
        exit()
    else:
        print("Please make a valid selection.")
    return coffee_selection


while True:
    run_coffee_cycle()


