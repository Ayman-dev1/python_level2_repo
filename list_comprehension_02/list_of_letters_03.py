# Create a new list of letters from a String
my_city = 'Cairo'
print('------------- normal way [ using loop ] ------------')
new_list = []
for letter in my_city:
    new_list.append(letter)

print(new_list)

print('------------- using List Comprehension ------------')
my_city = 'Cairo'
new_list = [letter for letter in my_city]
print(new_list)
