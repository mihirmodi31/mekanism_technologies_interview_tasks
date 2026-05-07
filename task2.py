#csv file code
#completed


temp_list = []
temp_flag = True
result_dict = {}

import csv
with open('data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        # print(lines)
        if temp_flag == True:
            temp_flag = False
            continue

        list_index_counter = 0
        temp_dict = {
            "id": lines[0],
            "user_id": lines[1],
            "amount": lines[2],
            "status": lines[3]
        }
        temp_list.append(temp_dict)

# for i in temp_list:
#     print(i)
# print()

id_list = []
total_amount_list = []
trasaction_count_list = []

for i in temp_list:
    if i["amount"] != 'invalid' and i["status"] == 'completed':
        # print(i)
        index = 0
        if i["user_id"] not in id_list:
            id_list.append(i["user_id"])
            total_amount_list.append(0)
            trasaction_count_list.append(0)
            index = id_list.index(i["user_id"])
        else:
            index = id_list.index(i["user_id"])
        total_amount_list[index] = total_amount_list[index] + int(i["amount"])
        trasaction_count_list[index] = trasaction_count_list[index] + 1


print(id_list)
print(total_amount_list)
print(trasaction_count_list)


        # temp_dict[i["user_id"]] = temp_dict[i["user_id"]].get(temp_dict["user_id"]["total_amount"], 0) + i["amount"]
