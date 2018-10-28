items = ["Com","Chao","Pho"]
# print(*items, sep = "," )
# x=input("Them vao:")
# items.append(x)            # Create 1 phan tu moi
# print(*items, sep = "," )

#print(items[0]) # Read

# items[0] = "Com rang" # Update
# print(items)

# print(items)
# items.pop(1)  # Delete 1 phan tu
# print(items)

# print (items)
# items.remove("Com") # Delete 1 phan tu
# print(items)

# print(items)
# i = int(input("Index:"))             # Update
# new_value = input("New value: ")
# items[i - 1] = new_value
# print(*items, sep ="\n")

print(items)
i = int(input("Index:"))             # Delete
items.pop(i - 1)
print(*items, sep ="\n")