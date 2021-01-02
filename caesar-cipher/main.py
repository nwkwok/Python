import sys
from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

run = False

start = input('Would you like to encode/decode something today? Type Y/N \n').lower()
if start == 'y':
    run = True
elif start == 'n':
    run = False
    print('\nCome back when you need something else encoded/decoded!')
    sys.exit()
else:
    print('Please select "y" or "n":\n')

while run:

    caesar_type = False

    while not caesar_type:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
        if direction == 'encode' or direction == 'decode':
            caesar_type = True
        else:
            print('Sorry, please type "encode" or "decode":\n')
            rerun = input("Want to try again? Type Y/N\n").lower()
            if rerun == 'n':
                print('\nCome back when you need something else encoded/decoded!')
                sys.exit()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if type(shift) != int:
        print('\nSorry, please type insert an integer:\n')
        rerun = input("Want to try again? Type Y/N\n").lower()
        if rerun == 'y':
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
        else:
            print('\nCome back when you need something else encoded/decoded!')
            sys.exit()

    def caesar(start_text, shift_amount, cipher_direction):
        cipher = ''
        if cipher_direction == 'decode':
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                position += shift_amount
                cipher += alphabet[position]
            else:
                cipher += char

        print(f"The {cipher_direction}d word is {cipher} \n \n")


    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    close = input("Would you like to run another cipher? Type Y/N:\n").lower()
    if close == 'n':
        run = False
        print('Come back when you need something else encoded/decoded!')