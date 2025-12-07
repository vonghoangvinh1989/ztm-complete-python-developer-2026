# formatted strings
name = 'Johnny'
age = 55

# print('hi ' + name + '. You are ' + str(age) + ' years old')
print(f'hi {name}. You are {age} years old')

# old way, .format could be use but could be complicated
print('hi {}. You are {} years old'.format(name, age))
print('hi {1}. You are {0} years old'.format(name, age))
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))

# Note: recommand to use f string