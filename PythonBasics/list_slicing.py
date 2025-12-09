# List Slicing
amazon_cart = ['notebooks', 
               'sunglasses',
               'toys',
               'grapes'
               ]

amazon_cart[0] = 'laptop'
# new_cart = amazon_cart // copy address
new_cart = amazon_cart[:] # create new list and assign
new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart)