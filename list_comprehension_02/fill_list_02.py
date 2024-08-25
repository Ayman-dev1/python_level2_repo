# fill a list with numbers from 1 to 10
print('------------- normal way [ using loop ] ------------')
numbers_list = []
for i in range(1, 11):
    numbers_list.append(i)

print(numbers_list)

print('------------- using List Comprehension ------------')
numbers_list = [i for i in range(1, 11)]

print(numbers_list)
