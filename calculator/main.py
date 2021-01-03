from art import logo
import os


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    is_calculating = True

    first_number = float(input('What is your first number?\n'))
    for key in operation:
        print(key)

    while is_calculating:
        operation_selection = input('Pick an operation\n')
        second_number = float(input('What is the next number?\n'))
        calculation_function = operation[operation_selection]
        answer = calculation_function(first_number, second_number)
        print(f"{first_number} {operation_selection} {second_number} = {answer}")
        next_operation = input(f'Type "y" to continue calculating with {answer} or type "n" to start a new calculator\n').lower()
        if next_operation == 'y':
            first_number = answer
        if next_operation == 'n':
            os.system('clear')
            is_calculating = False
            calculator()


calculator()


