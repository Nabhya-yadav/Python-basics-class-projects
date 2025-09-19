height=float(input("Enter your height in meters"))
weight=float(input("Enter your weight in kg"))

bmi=weight/height**2

print("Your bmi is",bmi)

if bmi<18.5:
    print("underweight")

elif bmi>=18.5 and bmi<=24.9:
    print("normal")

elif bmi>=25.0 and bmi<=29.9:
    print("overweight")

else:
    print("obeese")


