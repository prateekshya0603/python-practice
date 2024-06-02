#Write a program that takes three integers as input and determines the largest number among them.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print(num1, "is largest")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest")
else:
    print(num3, "is the largest")