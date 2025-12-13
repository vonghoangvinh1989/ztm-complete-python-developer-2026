# dictionary key always needs to be immutable
# key in dictionary needs to be unique
# same key will be overrided
dictionary = {
	'123': [1, 2, 3],
	'123': 'hello',
}

# a list can not be a key because it will be mutable
print(dictionary['123'])