x = int(input("your height (cm) = "))
y = int(input("your weight (kg) = "))
z = x/100
bmi = y/(z*z)
if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

