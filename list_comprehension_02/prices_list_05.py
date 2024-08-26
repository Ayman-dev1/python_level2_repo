# append prices to a new list if prices are valid, else append 'Invalid price'


prices_list = [300, 150, 160, -80, 250, -60, 400]
print('------------- normal way [ using loop ] ------------')
valid_prices_list = []
for item in prices_list:
    if item > 0:
        valid_prices_list.append(item)
    else:
        valid_prices_list.append('Invalid price')

print(valid_prices_list)

print('------------- using List Comprehension -------- Ternary operator ----')
prices_list = [300, 150, 160, -80, 250, -60, 400]
valid_prices_list = [item if item > 0 else 'invalid price' for item in prices_list]

print(valid_prices_list)

print('--------------- convert this code to a function and use it in a list comprehension  ---------------------')


def check_price(price):
    if price > 0:
        return price
    else:
        return 'invalid price'


prices_list = [300, 150, 160, -80, 250, -60, 400]
valid_prices_list = [check_price(item) for item in prices_list]
print(valid_prices_list)
