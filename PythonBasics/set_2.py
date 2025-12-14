my_set = {1, 2, 3, 4, 5, }
your_set = {4, 5, 6, 7, 8, 9, 10}

# tell the difference between my_set and your_set in the view of my_set
# not changing the original value of my_set
print(my_set.difference(your_set))
print(my_set)

# remove element from original set
# print(my_set.discard(5))
# print(my_set)

# get the difference and update to original my_set
# print(my_set.difference_update(your_set))
# print(my_set)

# return the intersection between these two
# print(my_set.intersection(your_set))
print(my_set & your_set) # short hand for intersection

# return True if two sets do not share any elements
# return False if at least one common element
print(my_set.isdisjoint(your_set))

# unite between two sets, remove any duplicate
# create new set
print(my_set.union(your_set))
print(my_set | your_set) # short hand of .union

my_set_2 = {4, 5, }
your_set_2 = {4, 5, 6, 7, 8, 9, 10}
print(my_set_2.issubset(your_set_2))

# your_set_2 cover all element of my_set_2
print(your_set_2.issuperset(my_set_2))
