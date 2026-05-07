# completed

transactions = [
   {"user_id": 1, "amount": 100},
   {"user_id": 2, "amount": 200},
   {"user_id": 1, "amount": 300},
   {"user_id": 3, "amount": 400},
   {"user_id": 2, "amount": 100},
   {"user_id": 1, "amount": 50}
]

iterator_temp = iter(transactions)

result_list = []
step_counter = 0
max_amount = 0
max_amount_user_id = 0

user_id_list = []
user_amount_list = []

def return_transaction_as_stream():
    for i in transactions:
        yield next(iterator_temp)

for i in range(6):
    temp_dict = {}
    temp_temp_dict = next(return_transaction_as_stream())
    index = 0
    # print(temp_temp_dict)
    if temp_temp_dict['user_id'] not in user_id_list:
        user_id_list.append(temp_temp_dict['user_id'])
        index = user_id_list.index(temp_temp_dict['user_id'])
        user_amount_list.append(0)
    else:
        index = user_id_list.index(temp_temp_dict['user_id'])
    user_amount_list[index] = user_amount_list[index] + temp_temp_dict['amount']
    if user_amount_list[index] >= max_amount:
        max_amount = user_amount_list[index]
        max_amount_user_id = temp_temp_dict['user_id']
    step_counter = step_counter + 1
    temp_dict["step"] = step_counter
    temp_dict["top_user"] = max_amount_user_id
    result_list.append(temp_dict)

# print(result_list)
# print()
# print(user_id_list)
# print(user_amount_list)
# print()

for i in result_list:
    print(i)