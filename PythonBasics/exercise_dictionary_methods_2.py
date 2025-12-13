user = {
	'age': 0,
	'username': '',
	'weapons': None,
	'is_active': False,
	'clan': None,
}

print(user.keys())

user['weapons'] = 'lightning sword'
print(user)

user.update({'is_banned': False})
# user['is_banned'] = False
print(user)

user['is_banned'] = True
print(user)

user2 = user.copy()
user2.update({'age': 20, 'username': 'vinhvong'})
print(user2)
