a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourth number:"))

def add(a, b, c, d):
    return a+ b+ c+ d

def mult(num1, num2, num3, num4):
    return num1* num2* num3* num4

def sub(a, b, c, d):
    return (a+b)- (c+d)

def callFunction(a, b, c, d):
    sum = add(a, b, c, d)
    print(sum)

    mul = mult(a, b, c, 5)
    print(mul)

    subtract = sub(a, b, c, d)
    print(subtract)

callFunction(a,b,c,d)
