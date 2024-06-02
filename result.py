marks = int(input("Enter your marks :"))

if marks == 75:
    print("Distinction")
    if marks >= 90:
        print("Topper")
    elif marks >= 80:
        print("Middle")
elif marks >= 60 and marks < 75:
    print("First division")
elif marks >= 45 and marks < 60:
    print("Second division")
else:
    print("Fail")

