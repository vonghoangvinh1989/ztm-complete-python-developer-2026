# print(True == 1) # True
# print('' == 1) # False
# print([] == 1) # False
# print(10 == 10.0) # True
# print([1,2,3] == [1,2,3]) # True

# == check for equality of value, it converts and check for the value 

# is: actually checks if the location in memory where this value is stored is the same
print(True is True)
print('1' is '1')
print([] is [])
print(10 is 10)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a == b)

# == check for value
# is check for location in memory, or check they are the same object