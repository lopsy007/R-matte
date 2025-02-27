import derivasjon_numerisk as plot
import numpy as np
import matplotlib.pyplot as plt
import math




x = np.linspace(-10, 10, 100)
f = lambda x: math.e**(-x**2)


plot.plot_same(x, f(x), 'f(x)=e^(-x^2)')	
plot.plot_same(x, plot.f_derivative(x, 0.01, f), 'f\'(x)')
plot.plot_same(x, plot.f_2derivative(x, 0.01, f), 'f\'\'(x)')
plt.title('f(x), f\'(x) and f\'\'(x)')
plt.legend()
plt.show()