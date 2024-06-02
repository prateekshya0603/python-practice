weight = (float(input("Enter your weight :")))
height = float(input("Enter your height :"))

bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >=25 and bmi < 30:
    print("Genda")
else:
    print("Bhaluuuu")