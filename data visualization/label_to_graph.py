import matplotlib.pyplot as plt

x = [1,2,3]
y = [4,5,6]

plt.plot(x,y,'g', label="line", linewidth="2")
plt.title("Simple Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
