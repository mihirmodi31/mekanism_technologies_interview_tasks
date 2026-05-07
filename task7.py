temp_dict = {
 "user": {
   "id": 1,
   "profile": {
     "name": "John",
     "address": {
       "city": "NY"
     }
   }
 }
}

next_part = tuple(temp_dict["user"])
basic_str = "user"

temp_list = []

while True:
    if len(next_part) >= 0:
        print("yeah")
        for i in next_part:
            if tuple(temp_dict["user"])
        print(next_part)
        break

print(tuple(temp_dict["user"]["profile"]))


# {
#  "user.id": 1,
#  "user.profile.name": "John",
#  "user.profile.address.city": "NY"
# }
