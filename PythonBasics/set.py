# set: unordered collection of unique objects
# set does not contain duplicate value even trying to add duplicate to it
my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)

# {1, 2, 3, 4, 5, 100}
print(my_set)

# generate error: set object is not subscriptable
# print(my_set[0])

print(1 in my_set)
print(len(my_set))
print(list(my_set))

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))

