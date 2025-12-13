# Dictionary
user = {
	'basket': [1, 2, 3],
	'greet': 'hello',
	'age': 20,
}

# 'i' in 'hi'
# print('basket' in user)
print('age' in user.keys())
print('hello' in user.values())

# items will wrap the entire key value
print(user.items())

user2 = user.copy()

# clear not return anything
# it just simple remove anything in dictionary
user.clear()
print(user)

# when user was clear, user2 still has the old info of user
print(user2)

user3 = {
	'basket': [1, 2, 3],
	'greet': 'hello',
	'age': 20,
}

# pop returns the value of whatever key put in of dictionary
print(user3.pop('age'))

# but when we print user3, 'age': 20 was popped out
print(user3)

# whatif we want to pop out the last item: key-value
# before python 3.7, it pop out randomly the whole item key-value
# but with python 3.7, it will pop out the last item
print(user3.popitem())
print(user3)

user4 = {
	'basket': [1, 2, 3],
	'greet': 'hello',
	'age': 20,
}

# update the key value
print(user4.update({'age': 55}))
print(user4)