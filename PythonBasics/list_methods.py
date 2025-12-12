basket = [1, 2, 3, 4, 5]

# METHODS relate to adding
# append function append to the end of list, not produce a result
# basket.append(100) 

# insert (index, value)
# new_list = basket.insert(5, 100)

# extend to adding a list [100, 101] --> allow iterable
# new_list = basket.extend([100])
# print(new_list)

# METHODS relate to removing
# pop removes the element of the end
# pop return the element will be removed

# basket.pop()
new_list = basket.pop(2)
print(new_list)

# we can use 'pop' with index value, it will pop the element at that index
basket.pop(0)
print(basket)

# remove function will accept the value inside, not the index
# remove will change the list in place, not return anything
new_list = basket.remove(4)
print(new_list)

# clear
# clear will remove all elements of list
# clear not return anythin
new_list = basket.clear()
print(basket)
print(new_list)

# append, insert change the list in place, not return anything
# append to the end, insert with (index, value)
# pop will give the result of element was popped out
# pop default will pop the end, but in pop with index
# remove, clear will not return anything
# remove will remove with value
# clear everything, no need parameter

# So: new_list = basket.append(100) --> new_list turns out None