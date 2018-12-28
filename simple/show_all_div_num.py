
def div_num(start, end, num):
    print(num, "divide number : ", end="")
    for x in range(start, end+1):
        if x % num == 0:
            print(x,",", end="")
        else:
            pass

start = int(input("Enter start point : "))
end = int(input("Enter end point : "))
num = int(input("Enter divider : "))

div_num(start, end, num)