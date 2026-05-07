# completed

data = [1,2,3,2,4,5,1,6,3,7,8,5]

def find_unique_elements(data):
    temp_set = set()
    result = []
    dupliate_count = 0
    for number in data:
        if number not in temp_set:
            temp_set.add(number)
            result.append(number)
        else:
            dupliate_count = dupliate_count + 1
    # print("result: ",end=" ")
    # print(result)
    # print("duplicate_count: ",end=" ")
    # print(dupliate_count)
    result_dic = {"unique": result, "duplicates_removed": dupliate_count}
    print(result_dic)

find_unique_elements(data)