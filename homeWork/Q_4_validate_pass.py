def password_validation(pass_value):
    count_upper, count_lower, count_digits, count_signs = 0, 0, 0, 0

    if len(pass_value) > 8:
        for letter in pass_value:
            if letter.isupper():
                count_upper += 1
            elif letter.islower():
                count_lower += 1
            elif letter.isdigit():
                count_digits += 1
            elif not letter.isalnum():
                count_signs += 1
        return count_lower >= 1 and count_upper >= 1 and count_signs >= 1 and count_digits >= 1
    return False


# Reading passwords from the file
with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\read_passwords - copy.txt", 'r') as my_file:
    content = [item.strip() for item in my_file]

# Filtering and writing valid passwords using list comprehension
with open("D:\\courses to learn\\Python Backend (senior steps)\\my_files\\valid_passwords - copy.txt", 'w') as my_file:
    my_file.writelines([item + '\n' for item in content if password_validation(item)])
