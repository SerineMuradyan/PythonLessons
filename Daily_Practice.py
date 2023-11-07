
# tup = ()
# while True:
#     n = input('Enter a number: ')
#     if n == '':
#         break
#     n = int(n)
#     tup += (n,)
# print('The tuple is', tup)
# for i in set(tup):
#     x = tup.count(i)
#     if x == 1:
#         print(f'{i} is a unique number.')

# ============================================================================

# tup = ()
# while True:
#     n = input('Enter a number: ')
#     if n == '':
#         break
#     n = int(n)
#     tup += (n,)
# print('The tuple is', tup)

# tup = set(tup)
# print(tup)


# tup = (5, 5, 5, 4, 4, 120, 4)

# s = set(tup)
# print(f'The unique number is {int((3 * sum(s) - sum(tup)) / 2)}')

# tup = (3, 4, 5, 10, 11)

# target = 9

# for i in range(len(tup)-1):
#     for j in range(i + 1, len(tup)):
#         if tup[i] + tup[j] == target:
#             print(i, j)

# nums = (-1, 0, 1, 2, -1, -4)

# target = 0

# for i in range(len(nums) - 2):
#     for j in range(i + 1, (len(nums)- 1)):
#         for k in range(j + 1, (len(nums))):
#             if nums[i] + nums[j] + nums[k] == target:
#                 print(nums[i], nums[j], nums[k])


