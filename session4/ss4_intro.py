# person = ["H.Duc", "Hai Phong", "FTU", 23, 3, 257, False]

# person = {}
# print(person)
# print(type(person))

# person = {
#     "name": "H.Duc"
# }
# print(person)
# print(type(person))

person = {
    "name": "H.Duc",
    "location": "Hai Phong",
    "age": 23
}
# print(person)
# person["friend_count"]= 257
# print(person)

key = "name"
if key in person:
    print(person[key])
else:
    print("Not found")