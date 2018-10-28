items = ["T-Shirt", "Sweater"]
n = input("Welcome to our shop, what do you want (C, R, U, D): ")
if n == "R":
    print("Our items: ", *items, sep = ",")
if n == "C":
    new = input("Enter new item: ")
    items.append(new)
    print("Our items: ", *items, sep = ",")
if n == "U" :
    x = int(input("Update position: "))
    y = input("New item: ")
    items[x - 1] = y
    print("Our items: ", *items, sep = ",")
if n == "D":
    d = int(input("Delete position: "))
    items.pop(d - 1)
    print("Our items: ", *items, sep = ",")