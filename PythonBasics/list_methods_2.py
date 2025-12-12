basket = ['a', 'b', 'c', 'd', 'e', 'd']

# index (index, start, stop)
# find the value 'd' from index 0 to 1 (not include index 2)
# print(basket.index('d', 0, 2))
print(basket.index('d', 0, 6))

# keyword 'in'
print('d' in basket)
print('x' in basket)
print('i' in 'hi my name is Ian')

# count, 'd' appears 1 in list
print(basket.count('d'))