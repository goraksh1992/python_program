
def rev_number():
    num = input("Enter number : ")

    for n in range(1,len(num)+1):
        print(num[-n], end="")

rev_number()