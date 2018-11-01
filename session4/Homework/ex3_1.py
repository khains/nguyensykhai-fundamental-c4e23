print("Answer the following algebra question:")
print("If x=8, then what is the value of 4(x + 3) ?")
d = {
    "1" :35,
    "2" :36,
    "3" :40,
    "4" :44,
}
for k,v in d.items():
   print(k,".", v)
x = int(input("Your choice: "))
if x == 4:
    print("Bingo")
else:
    print(":(")
