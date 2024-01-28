# Prompt: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

user_str = input('Please enter a word. ')
print(f'user_str: {user_str}')

user_str_rev = user_str[::-1]
print(f'user_str_rev: {user_str_rev}')

print(f'"{user_str}" is a palindrome.') if user_str == user_str_rev else print(f'"{user_str}" is not a palindrome.')