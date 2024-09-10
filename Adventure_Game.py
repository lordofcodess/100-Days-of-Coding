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

print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M or L ')
add_pepperoni = input('Do you want pepperoni? Y or N ')
extra_cheese = input('Do you want extra cheese? Y or N ')

if size == 'S':
    price = 15
    if add_pepperoni == 'Y':
        price += 2
    if extra_cheese == 'Y':
        price += 1
    print(f'The final bill is ${price}')
elif size == 'M':
    price = 20
    if add_pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
    print(f'The final bill is ${price}')
elif size == 'L':
    price = 25
    if add_pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
    print(f'The final bill is ${price}')