import matplotlib.pyplot as plt
import numpy as np
import plotting as plot

# Define the lambda function
f = lambda x: x**3+2*x

x, y = plot.generate_x_y(f, -10, 10, 400)
plot.plot_same(x, y, 'f(x) = x^3+2x')
plot.plot_same(y, x, 'f^-1(x)')
plot.plot_same(x, x, 'y=x', -10, 10, -10, 10)
plt.show()