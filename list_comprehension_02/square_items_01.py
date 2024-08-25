# append all items from my_list after square the items to new_list
# normal way [using loop]
print('----- normal way [using loop] ------')
my_list = [1, 2, 3, 4]
new_list = []
for item in my_list:
    new_list.append(item ** 2)

print(new_list)
print('-------- using List Comprehension -----------')
my_list = [1, 2, 3, 4]
wew_list = [item ** 2 for item in my_list]
print(wew_list)
