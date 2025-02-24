import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def f_derivative(x, h):
    return (f(x+h) - f(x))/h

def f_2derivative(x, h):
    return (f_derivative(x+h, h) - f_derivative(x, h))/h

h = 0.01
x = np.linspace(-10, 10, 100)

plt.plot(x, f(x), label='f(x) = x^2')
plt.plot(x, f_derivative(x, h), label="f'(x) = 2x")
plt.plot(x, f_2derivative(x, h), label="f''(x) = 2")

plt.title('Graph of x^2 and its derivatives')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()

