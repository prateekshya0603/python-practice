num = int(input("Enter a number: "))
def palindromeNumber(num):
    if num == num[::-1]:
        print("The number is palindrome")
        return True