# Dictionary
user = {
	'basket': [1, 2, 3],
	'greet': 'hello',
	'age': 20,
}

# use .get method and put the key inside
# if the key is not exist, it will give the result 'None'
# it will not generate error
print(user.get('age'))

# we can add the default value with .get
# in case 'age' does not exist, the default value will be used, here is 55
print(user.get('age', 55))

# another way to create dictionary
user2 = dict(name='JohnJohn')
print(user2)