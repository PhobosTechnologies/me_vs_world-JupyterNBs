import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

X = np.linspace(0, 365)
Y = np.cos(X)

fig, ax = plt.subplots()
ax.plot(X, Y, color='C1')
fig.savefig("figure.pdf")
fig.show()
