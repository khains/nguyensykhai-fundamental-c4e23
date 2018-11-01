x = input("Enter a string: ").lower()
y = 1
xx = sorted(set(x))
print(xx) 
for i in range(len(xx)):
    char = xx[i]
    print(char, x.count(char), sep="  ")