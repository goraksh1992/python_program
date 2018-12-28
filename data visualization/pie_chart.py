
import matplotlib.pyplot as plt

slice = [7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c','m','r','b']

plt.pie(slice,
labels=activities, 
colors=colors, 
startangle=90, 
shadow=True, 
explode=(0,0.1,0,0), 
autopct='%1.1f%%')

plt.title("Pie Chart")
plt.show()