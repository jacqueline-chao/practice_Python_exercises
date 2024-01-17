# Prompt: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f'list_1: {list_1}')

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(f'list_2: {list_2}')

set_1 = set(list_1)
print(f'set_1: {set_1}')

set_2 = set(list_2)
print(f'set_2: {set_2}')

result_list = set_1 & set_2 # '&' or 'intersect' is a set operation
print(f'result_list: {result_list}')