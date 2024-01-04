# Prompt: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

# # Version 1:
# from random import sample

# nums = sample(range(0, 10), 10)

# print(nums)

# for num in nums:
#     if num < 5:
#         print(num)

# # Version 2:
# from random import sample

# nums = sample(range(0, 10), 10)
# select_nums = []

# print(f'nums: {nums}')
# print(f'select_nums: {select_nums}')

# for num in nums:
#     if num < 5:
#         select_nums.append(num)

# print(f'nums: {nums}')
# print(f'select_nums: {select_nums}')

# # Version 3:
# from random import sample

# nums = sample(range(0, 10), 10)

# print(f'nums: {nums}')

# select_nums = [num for num in nums if num < 5]

# print(f'select_nums: {select_nums}')

# Version 4:
from random import sample

nums = sample(range(0, 10), 10)
user_num = int(input('Please provide a number. '))

print(f'nums: {nums}')
print(f'user_num: {user_num}')

select_nums = [num for num in nums if num < user_num]

print(f'select_nums: {select_nums}')