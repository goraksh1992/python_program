
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

data = pd.read_csv("E:/python/python_program/data visualization/countries.csv")
print(data.head(5))
print(" ")
print(data.tail(5))

d = data.to_html('country.html') # create html file

p = plt.bar(data.year, data.population, label="population")
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Graph")
plt.grid(True, color="K")
plt.legend()
plt.show()