import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,'g', label="Line one", linewidth="2")
plt.plot(x2,y2,'c', label="Line two", linewidth="2")
plt.title("Simple Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, color="k")
plt.show()
