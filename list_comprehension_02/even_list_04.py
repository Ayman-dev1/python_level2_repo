# append only even numbers from my_list to even_list
my_list = [14, 5, 7, 10, 20, 15]
print('------------- normal way [ using loop ] ------------')
even_list = []
for item in my_list:
    if item % 2 == 0:
        even_list.append(item)

print(even_list)

print('------------- using List Comprehension ------------')
my_list = [14, 5, 7, 10, 20, 15]
even_list = [item for item in my_list if item % 2 == 0]
print(even_list)
