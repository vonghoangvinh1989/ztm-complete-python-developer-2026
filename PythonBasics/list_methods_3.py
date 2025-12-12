basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

# sort will sort the list in place, not return anything
basket.sort()

# sorted will be a function to sort the list put inside
# sorted will create a copy of basket, sorted and return new list, and will not change the original list
# basket will not be modified
# print(sorted(basket))
# print(basket)

# Note: What sorted does look like this
# new_basket = basket[:]
# new_basket = basket.copy()
# new_basket.sort()
# print(new_basket)
# print(basket)

# Note: copy function can use to copy a list
# instead of basket[:], we can use basket.copy()

# reverse will reverse the basket in place
# it will not sort, it just reverse
# basket.reverse()
print(basket)