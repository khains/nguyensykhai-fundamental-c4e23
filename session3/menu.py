# item1 = "Pho xao"
# item2 = "Ghe"
# item3 = "So huyet"
# item4 = "Chao"
# item5 = "Com rang"

# items = [] # Empty list
# print(type(items))

# items = ["Ghe"] # list 1 phan tu
# print(items)

items = ["Ghe", "So huyet"]
print(items)
new_item = "Com rang"
items.append(new_item)
print(*items, sep=",")
