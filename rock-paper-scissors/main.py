import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = ['rock', 'paper', 'scissors']
rps_length = len(rps)
random_rps = random.randint(0, rps_length-1)

computer_choice = rps[random_rps]
print(computer_choice)

user_input = input("What's it gonna be? Rock, paper or scissors?\n")
user_input = user_input.lower()

'You Selected: \n'
if user_input == 'rock':
    print(rock + "\n You selected rock!")
elif user_input == 'paper':
    print(paper + "\n You selected paper!")
elif user_input == 'scissors':
    print(scissors + "\n You selected scissors!")
else:
    print("R-O-C-K, P-A-P-E-R OR S-C-I-S-S-O-R-S... C\'mon... it\'s not that hard!")

'The computer selected \n'
if computer_choice == 'rock':
    print(rock + "\n The computer selected rock!")
elif computer_choice == 'paper':
    print(paper + "\n The computer selected paper!")
elif computer_choice == 'scissors':
    print(scissors + "\n The computer selected scissors!")

if user_input == 'rock':
    if computer_choice == 'scissors':
        text = "\nLooks like you win!"
    elif computer_choice == 'paper':
        text = "\nLooks like you lose!"
    else:
        text = "\nLooks like it\'s a draw!"

if user_input == 'paper':
    if computer_choice == 'rock':
        text = '\nLooks like you win!'
    elif computer_choice == 'scissors':
        text = '\nLooks like you lose!'
    else:
        text = "\nLooks like it\'s a draw!"

if user_input == 'scissors':
    if computer_choice == 'paper':
        text = '\nLooks like you win!'
    elif computer_choice == 'rock':
        text = '\nLooks like you lose!'
    else:
        text = "\nLooks like it\'s a draw!"

print(text)











