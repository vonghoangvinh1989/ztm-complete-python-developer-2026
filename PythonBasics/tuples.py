# Tuples
# Tuples are immutable (immutable list)
my_tuple = (1, 2, 3, 4, 5)

# generate error
# my_tuple[1] = 'z'

print(my_tuple[1])
print(5 in my_tuple)

user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user[(1, 2)])