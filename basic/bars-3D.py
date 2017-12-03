from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
# yticks = ["清华", "北大", "武大", "南开"]
yticks = [1,2,3,4]
for c, k in zip(colors, yticks):
    # Generate the random data for the y=k 'layer'.
    xs = ['r', 'g', 'b', 'y']
    ys = np.random.rand(4)     #z轴

    # You can provide either a single color or an array with the same length as
    # xs and ys. To demonstrate this, we color the first bar of each set cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('项目')
ax.set_ylabel('学校')
ax.set_zlabel('数量')

# On the y axis let's only label the discrete values that we have data for.
ax.set_yticks(yticks)

plt.show()
