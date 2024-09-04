# print('Hello'[0])
#
# number = input('Enter a two-digit number: ')
# a = int(number[0])
# b = int(number[1])
# print(a+b)

# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")
#
# height = float(height)
# weight = float(weight)
# bmi = weight/height**2
# print(int(bmi))

# age = input("Enter your age: ")
# age = int(age)
# total_days = 90 * 365
# total_weeks = 90 * 52
# total_months = 90 * 12
#
# days_left = total_days - (age*365)
# weeks_left = total_weeks - (age * 52)
# months_left = total_months - (age * 12)
#
# print(f'You have {days_left} days left, {weeks_left} weeks left, {months_left} months left')

print('Welcome to the tip calculator!')
Total_bill = float(input('What was the total bill? $'))

Tip_percent = input('What percentage tip would you like to give? 10, 12, or 15? ')
People = int(input('How many people to split the bill? '))

if Tip_percent == '10':
    Tip_bill = round(Total_bill/People * 1.10, 2)
    print(f'Each person should pay: ${Tip_bill}')
elif Tip_percent == '12':
    Tip_bill = round(Total_bill/People * 1.12, 2)
    print(f'Each person should pay: ${Tip_bill}')
elif Tip_percent == '15':
    Tip_bill = round(Total_bill/People * 1.15, 2)
    print(f'Each person should pay: ${Tip_bill}')

