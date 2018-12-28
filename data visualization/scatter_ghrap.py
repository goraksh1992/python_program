
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,4,2,1,4,5,2,3]

plt.scatter(x,y, color="r", label="skitcat")
plt.title("Scatter Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()