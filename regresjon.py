import plotting as plot
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2.1, 3.9, 6.5, 7.1, 11.0]

coefficients = np.polyfit(x, y, 1)

plt.scatter(x, y, color='red')
plt.plot(x, np.polyval(coefficients, x))
plt.show()
