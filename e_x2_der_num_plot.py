import derivasjon_numerisk as plot
import numpy as np
import matplotlib.pyplot as plt




x = np.linspace(-10, 10, 100)
f = lambda x: x**3


plot.plot_same(x, f(x), 'f(x)=x^3')
plot.plot_same(x, plot.f_derivative(x, 0.01, f), 'f\'(x)=3x^2')
plot.plot_same(x, plot.f_2derivative(x, 0.01, f), 'f\'\'(x)=6x')
plt.title('f(x), f\'(x) and f\'\'(x)')
plt.legend()
plt.show()