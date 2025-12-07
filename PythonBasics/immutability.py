# immutable: can not be change
selfish = '01234567'

# can not change the value of it when it created
# the only way to change it is reassigning the value
# selfish[0] = '8'
# print(selfish)

selfish = '8'
print(selfish)

# note: can not reassign part of string
selfish = selfish + '8' # this is a whole new string, not the same 'selfish' anymore
