yob_str = input("Year your birth:")
while not yob_str.isdigit():
    print("not OK")
    yob_str = input("Year your birth:")   
yob = int(yob_str)
age = 2018 - yob
print(age)