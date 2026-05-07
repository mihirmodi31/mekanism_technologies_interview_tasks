# completed

logs = [
   {"timestamp": 1, "event": "click"},
   {"timestamp": 2, "event": "click"},
   {"timestamp": 3, "event": "scroll"},
   {"timestamp": 7, "event": "click"},
   {"timestamp": 8, "event": "click"}
]

new_click_count = 0
new_scroll_count = 0

last_reminder = 0
low = 1
high = 5
# print(6//5)

result_list = []

for i in logs:
    if i["timestamp"] >= low and i["timestamp"] <= high:
        if i["event"] == "click":
            new_click_count = new_click_count + 1
        elif i["event"] == "scroll":
            new_scroll_count = new_scroll_count + 1
    else:
        temp_dic = {}
        temp_dic["window"] = str(low) + "-" + str(high)
        if new_click_count > 0:
            temp_dic["click"] = new_click_count
        if new_scroll_count > 0:
            temp_dic["scroll"] = new_scroll_count
        
        result_list.append(temp_dic)
        low = low + 5
        high = high + 5
        new_scroll_count = 0
        new_click_count = 0
        if i["event"] == "click":
            new_click_count = new_click_count + 1
        elif i["event"] == "scroll":
            new_scroll_count = new_scroll_count + 1

temp_dic = {}
temp_dic["window"] = str(low) + "-" + str(high)
if new_click_count > 0:
    temp_dic["click"] = new_click_count
if new_scroll_count > 0:
    temp_dic["scroll"] = new_scroll_count

result_list.append(temp_dic)

print()
print(result_list)
print()


# [

#  {"window": "1-5", "click": 2, "scroll": 1},
#  {"window": "6-10", "click": 2}
# ]
