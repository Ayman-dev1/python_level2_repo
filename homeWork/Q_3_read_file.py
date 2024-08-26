read_data = 'D:\\courses to learn\\Python Backend (senior steps)\\my_files\\read_data.txt'

with open(read_data, 'r') as file:
    my_list = [line for line in file]

print(" ".join(my_list))

