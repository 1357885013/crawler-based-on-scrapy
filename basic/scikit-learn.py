import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties()

plt.figure()
plt.title('this is title')
plt.xlabel('x label')
plt.ylabel('y label')
plt.axis([0, 10, 0, 10])  # x轴范围0-10，y轴范围0-10.
plt.grid(True)
x = [[1], [2], [3], [4], [5], [6]]
y = [[1], [2.1], [2.9], [4.2], [5.1], [5.8]]
plt.plot(x, y, 'c.')
plt.plot(x, y, 'g-')
# plt.plot(x,y,'c.',x,y,'g-')
plt.show()
