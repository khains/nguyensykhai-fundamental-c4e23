l_list = [
    {
        "#": 1,
        "name": "Huy",
        "hours": 30,
        "vnd per hour": 50,
    },
    {
        "#": 2,
        "name": "Quan",
        "hours": 20,
        "vnd per hour": 40,
    },
    {
        "#": 3,
        "name": "Duc",
        "hours": 15,
        "vnd per hour": 35,
    }
]

for i in l_list:
    print(i["hours"])

s = 0
for h in l_list:
    l = h["hours"]*h["vnd per hour"]
    s = s + l
print(s)
