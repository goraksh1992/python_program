
def swap():
    num1 = int(input("enter first num : "))
    num2 = int(input("Enter second num : "))

    print("Before swap num1 :", num1, "num2 : ", num2)

    num1  = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2

    print("After swap num1 :", num1, "num2 : ", num2)

swap()

