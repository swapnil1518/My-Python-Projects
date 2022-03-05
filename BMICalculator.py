# BMI = weight (kg)/height^2 (m^2)

w = float(input("enter weight in kg : "))
h = float(input("enter height in m : "))

BMI = w/(h**2)
print(BMI)

if BMI < 19:
    print("Thinness")
elif BMI > 19 and BMI < 25:
    print("Normal")
elif BMI > 25:
    print("Overweight")