n = int(input("Enter n:"))
m = int(input("Enter m:"))
for i in range(1, n * m + 1):
    print("*", end = "")
    if i % n ==0:
        print()