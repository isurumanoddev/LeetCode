import json

# data = """{
#     "name":"isuru",
#     "phone":{
#         "type":"intl",
#         "number":"0763222186"
#     },
#     "email":{"hide":"yes"}
# }
# """

# info = json.loads(data)
# print("Name : ",info["name"])
# print("Contact : ",info["phone"]["number"])
# print("Email : ",info["email"]["hide"])




input = """
    [
    {
    "id":"001",
    "x":"2",
    "name":"isuru  "
    },
    {
    "id":"002",
    "x":"3",
    "name":"Ann  "
    } ]
"""


info =json.loads(input)
print("usur count",len(info))
for i in info:
    print("Name : ",i["name"])
    print("Contact : ",i["id"])
    print("X : ",i["x"])
    print()