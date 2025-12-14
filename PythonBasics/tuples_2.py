# Tuple
my_tuple = (1, 2, 3, 4, 5, 5)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

new_tuple = my_tuple[1:4]
print(new_tuple)

x, y, z, *other = (1, 2, 3, 4, 5)

print(x)
print(y)
print(z)
print(other)

