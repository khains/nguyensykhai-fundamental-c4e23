s = input("Enter a text: ")
if (not s.islower()) and (not s.isupper()) and (not s.isdigit()):
    print("OK")
else:
    print("not OK")
