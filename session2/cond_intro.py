yob = int(input("your year of birth = "))
age = 2018 - yob
print(age)
if age <10:
    print("baby")
elif age<18:
    print("Teenager")
else:
    print("Adult")