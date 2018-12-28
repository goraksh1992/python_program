
import matplotlib.pyplot as plt

plt.bar([1,3,7,9,8],[5,2,7,8,2], label="Example one")
plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example one")

plt.title("Bar Graph", color="g")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
#plt.grid(True, color="k")
plt.show()