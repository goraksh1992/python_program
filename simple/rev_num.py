
class Rev_Number:

    def __init__(self, num):
        self.num = num

    def rev(self, num):
        rev = 0
        while num > 0:
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10
        print("Reverse number:",rev)

num = int(input("Enter number : "))

obj = Rev_Number(num)
obj.rev(num)

        