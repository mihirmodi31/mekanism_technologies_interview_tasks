# completed

file_path = 'logs.txt'

temp_list = []

with open(file_path, 'r') as file:
    # file_content = file.read()
    # print(file_content)
    file_lines = file.readlines()
    for line in file_lines:
        temp_line = line.strip()
        # print(temp_line)
        temp_list.append(temp_line.split())

# print()
# print(temp_list)

total_error_count = 0
errors_per_user_id_list = []
errors_per_user_value_list = []

for i in temp_list:
    if i[0] == "ERROR":
        total_error_count = total_error_count + 1
        if i[5] not in errors_per_user_id_list:
            errors_per_user_value_list.append(0)
            errors_per_user_id_list.append(i[5])
            index = errors_per_user_id_list.index(i[5])
        else:
            index = errors_per_user_id_list.index(i[5])
        errors_per_user_value_list[index] = errors_per_user_value_list[index] + 1

print()
print(total_error_count)
print(errors_per_user_id_list)
print(errors_per_user_value_list)
print()

