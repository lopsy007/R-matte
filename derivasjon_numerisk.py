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

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(x, f(x), label='f(x) = x^2')
plt.title('f(x) = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-10, 10)
plt.ylim(-20, 100)

plt.subplot(1, 3, 2)
plt.plot(x, f_derivative(x, h), label="f'(x) = 2x")
plt.title("f'(x) = 2x")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-10, 10)
plt.ylim(-20, 100)

plt.subplot(1, 3, 3)
plt.plot(x, f_2derivative(x, h), label="f''(x) = 2")
plt.title("f''(x) = 2")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-10, 10)
plt.ylim(-20, 100)

plt.show()

