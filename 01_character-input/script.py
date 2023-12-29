# Prompt: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

user_name = input('Please enter your first name. ')
user_age = int(input('Please enter your age in years. '))
user_number = int(input('Please enter a number. '))

curr_year = 2023
rem_years = 100 - user_age

hund_year = curr_year + rem_years

text = 'You, ' + user_name + ', will turn 100 years old in the year ' + str(hund_year) + '.'

for i in range(user_number):
    print(text)