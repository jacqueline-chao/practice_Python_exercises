# Prompt: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

# Assumptions:
# - The value of user_number is zero or a positive integer.

# Test Cases:
# - user_number: 0
# - user_number: 1
# - user_number: 2
# - user_number: 3
# - user_number: 4
# - user_number: 5
# - user_number: 9

from sys import exit

user_number = int(input('Please enter a number. '))
print(f'user_number: {user_number}')

if user_number == 0:
    print(f'{user_number} has no divisors.')
    exit(0)

possible_divisors = set(range(1, ((user_number // 2) + 1), 1)) | {user_number}
print(f'possible_divisors: {possible_divisors}')

divisors = []
for divisor in possible_divisors:
    if user_number % divisor == 0:
        divisors.append(divisor)
print(f'divisors: {divisors}')