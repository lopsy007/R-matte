import plotting as plot
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit




x = [1, 2, 3, 4, 5]
y = [2.1, 3.9, 6.5, 7.1, 11.0]

# Using scipy
def f(x, a, b):
    return a*x + b
koeffisienter, kovarians = curve_fit(f, x, y)
print(koeffisienter)


# Using numpy
coefficients = np.polyfit(x, y, 1)

plt.scatter(x, y, color='red')
plt.plot(x, np.polyval(coefficients, x))
plt.show()
