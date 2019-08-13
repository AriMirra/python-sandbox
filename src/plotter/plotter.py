# you will need to install matplotlib (pip install matplotlib)
import matplotlib.pyplot as plt

x1, y1 = 1, 1
x2, y2 = 3, 2

x3, y3 = 0, 2

plt.plot([x1], [y1], 'ro-')
plt.pause(1)
plt.plot([x1, x2], [y1, y2], 'ro-')
plt.pause(1)

plt.plot([x1, x2, x3], [y1, y2, y3], 'ro-')
plt.pause(1)

plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'ro-')
plt.pause(1)

plt.show()

