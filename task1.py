# completed

dataset = [
 {"user_id": 1, "amount": 100},
 {"user_id": 2, "amount": 200},
 {"user_id": 1, "amount": 150},
 {"user_id": 3, "amount": 300},
 {"user_id": 2, "amount": -50},
 {"user_id": "null", "amount": 500},
 {"user_id": 4, "amount": "invalid"}
]

result_dic = {"totals": {}, "top_spender": 0}
top_spender_amount = 0

for i in dataset:
    if i["user_id"] != "null" and i["amount"] != "invalid":
        result_dic["totals"][i["user_id"]] = result_dic["totals"].get(i["user_id"], 0) + i["amount"]
        if result_dic["totals"][i["user_id"]] > top_spender_amount:
            result_dic["top_spender"] = i["user_id"]
            top_spender_amount = result_dic["totals"][i["user_id"]]



print()
print(result_dic)
print()
print()
