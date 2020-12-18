#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = ''
password_numbers = ''
password_symbols = ''

for letter in range(1, (nr_letters+1)):
    password_letters += letters[random.randint(0, len(letters)-1)]

for number in range(1, (nr_numbers+1)):
    password_numbers += numbers[random.randint(0, len(numbers)-1)]

for symbol in range(1, (nr_symbols+1)):
    password_symbols += symbols[random.randint(0, len(symbols)-1)]

#Eazy Level - Order not randomised:
easy_password = password_letters + password_numbers + password_symbols
print(easy_password)

#Hard Level - Order of characters randomised:
hard_password_list = [password_letters, password_numbers, password_symbols]
shuffled = random.sample(hard_password_list, len(hard_password_list))
hard_password = shuffled[0] + shuffled[1] + shuffled[2]
print(hard_password)

