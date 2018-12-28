
import matplotlib.pyplot as plt

a_price = [100,120,130,140,150,160]
m_price = [120,130,140,150,160,170]
year = [2000,2001,2002,2003,2004,2006]

fig_1 = plt.figure(1, figsize=(10,5))

apple_price = fig_1.add_subplot(121)
microsoft_price = fig_1.add_subplot(122)

apple_price.plot(year, a_price)
microsoft_price.plot(year, m_price)

plt.show()
