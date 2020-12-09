print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
start = input("Are you ready to begin? Y or N?\n")

if start.lower() == 'y':
    print("Here we go!")
    step1 = input("left or right?\n")
    if step1.lower() == 'left':
        step2 = input("Getting warmer. Swim or wait?\n")
        if step2.lower() == 'wait':
            step3 = input("Whew! Those trout looked hungry! Now which door?\n Red, Blue or Yellow?\n")
            if step3.lower() == 'yellow':
                print("Congratulations! You've found the hidden treasure!")
            elif step3.lower() == 'red':
                print('Red = Fire. You were burned by fire... Game over!')
            elif step3.lower() == 'blue':
                print('Yikes. You were eaten by beasts. Game over!')
            else:
                print('I guess you are color blind... Game over!')
        elif step2.lower() == 'swim':
            print("Oh no... You were attacked by trout. Game over!")
        else:
            print("You were stampeded by wild boar. Should've swam or waited!")
    elif step1.lower() == 'right':
        print("Oops. You fell into a hole. Game over!")
    else:
        print("You got confused on which direction to go so you decided to back your bags and go home")
elif start.lower() == 'n':
    print("Okay, maybe when you're feeling a little bit more adventerous")
else:
    print("It can't be that hard to follow instructions... can it?")
