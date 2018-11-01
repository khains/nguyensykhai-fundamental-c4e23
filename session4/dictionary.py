x = {
    "cat": "meo",
    "dog": "cho",
    "bird": "chim",
    "fish": "ca",
}
# key = ["cat", "dog", "bird", "fish"]
# print(*key)
while True:
    key1 = input("key: ")
    if key1 in x:
        print("Translation: ", x[key1])
    else:
        add=input("Not found, do you want to contribute this word? (Y/N)?").upper()
        if add ==  "N" or add == "NO" :
            break
        if add == "Y" or add == "YES":
            x[key1] = input("Translation: ")
            print(x)
# while n not in key:
#     print("Not found")
#     n = input("key: ")
# print("Translation: ", x[n])