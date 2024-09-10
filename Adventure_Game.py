# number = int(input('What number do you want to check?: '))
# if number % 2 == 0:
#     print(f'{number} is an even number.')
# else:
#     print(f'{number} is an odd number.')

#Bmi

# weight = float(input('Enter your weight in kg: '))
# height = float(input('Enter your height in m: '))
#
# bmi = round(weight / height ** 2)
#
# if bmi < 18.5:
#     print(f'Your bmi is {bmi}, you are underweight.')
# elif bmi < 25:
#     print(f'Your bmi is {bmi}, you are normal.')
# elif bmi < 30:
#     print(f'Your bmi is {bmi}, you are overweight.')
# elif bmi < 35:
#     print(f'Your bmi is {bmi}, you are obese.')
# else:
#     print(f'Your bmi is {bmi}, you are clinically obese.')

# leap year

# number = int(input("Enter the year: "))
#
# if number % 4 != 0:
#     print('Not leap year')
# else:
#     if number % 100 != 0:
#         print('Leap year')
#     else:
#         if number % 400 == 0:
#             print('Leap year')
#         else:
#             print('Not leap year')
#
# print('Welcome to Python Pizza Deliveries!')
# size = input('What size pizza do you want? S, M or L ')
# add_pepperoni = input('Do you want pepperoni? Y or N ')
# extra_cheese = input('Do you want extra cheese? Y or N ')
#
# if size == 'S':
#     price = 15
#     if add_pepperoni == 'Y':
#         price += 2
#     if extra_cheese == 'Y':
#         price += 1
#     print(f'The final bill is ${price}')
# elif size == 'M':
#     price = 20
#     if add_pepperoni == 'Y':
#         price += 3
#     if extra_cheese == 'Y':
#         price += 1
#     print(f'The final bill is ${price}')
# elif size == 'L':
#     price = 25
#     if add_pepperoni == 'Y':
#         price += 3
#     if extra_cheese == 'Y':
#         price += 1
#     print(f'The final bill is ${price}')

# print('Welcome to the love calculator!')
# name1 = input('What is your name? \n')
# name2 = input('What is their name? \n')
#
# name1 = name1.lower()
# name2 = name2.lower()
#
# name = name1 + name2
#
# T = name.count('t')
# R = name.count('r')
# U = name.count('u')
# E = name.count('e')
# L = name.count('l')
# O = name.count('o')
# V = name.count('v')
#
# number_one = T + R + U + E
# number_two = L + O + V + E
#
# final_number = int(str(number_one) + str(number_two))
#
# if final_number < 10 or final_number > 90:
#     print(f'Your score is {final_number}, you go together like coke and mentos.')
# elif 40 <= final_number <= 50:
#     print(f'Your score is {final_number}, you are alright together.')
# else:
#     print(f'Your score is {final_number}.')

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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************

''')

print('Welcome to Treasure Island')
print('Your mission is to find the treasure')

left_or_right = input('You have crossed the first sea. You are now at a crossroad. Where do you want to go? left or '
                      'right? \n')
left_or_right = left_or_right.lower()

if left_or_right == 'left':
    swim_or_wait = input("You are on the right path. You can wait for reinforcement or continue. Swim or wait? \n")
    swim_or_wait = swim_or_wait.lower()
    if swim_or_wait == 'swim':
        print('Game Over.')
    else:
        cave = input('Reinforcements available. You can continue. Select a cave. Red, Blue or Yellow? \n')
        cave = cave.lower()
        if cave == 'red':
            print('Game Over')
        elif cave == 'blue':
            print('Game Over')
        else:
            print('You Win!')
else:
    print('Game Over.')



