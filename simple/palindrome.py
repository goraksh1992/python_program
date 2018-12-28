
num = int(input("Enter number : "))
n = num
rev = 0
a = []
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
a.append(rev)

if n == a[0]:
    print(n, "is palindrome")
else:
    print(n, "is not palindrome") 
