# Prompt: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# Version 1:
# user_number = int(input('Please enter a number. '))

# if user_number % 2 == 0:
#     print('You entered an even number.')
# else:
#     print('You entered an odd number.')

# Version 2:
user_number = int(input('Please enter a number. '))

is_even = (user_number % 2 == 0)

text = 'You entered an even number.' if is_even else 'You entered an odd number.'

print(text)