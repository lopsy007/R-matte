import numpy as np
import matplotlib.pyplot as plt
from typing import Callable


def f_derivative(x, f, h=0.001):
    return (f(x+h) - f(x))/h

def f_2derivative(x, f, h=0.001):
    return (f_derivative(x+h, f, h) - f_derivative(x, f, h))/h

def plot_sub(x, y, title, total_plots, plot_number, min_x=None, max_x=None, min_y=None, max_y=None):
    plt.subplot(1, total_plots, plot_number)
    plt.plot(x, y, label=title)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.xlim(-10, 10)
    plt.ylim(-100, 100)

def plot_same(x, y, title="f(x)", min_x=None, max_x=None, min_y=None, max_y=None):
    plt.plot(x, y, label=title)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)

    if min_x and max_x:
        plt.xlim(min_x, max_x)
    if min_y and max_y:
        plt.ylim(min_y, max_y)

def plot_same_with_derivatives(
        f:Callable[[float], float],
        x_start:int, 
        x_end:int, 
        x_count:int=100,
        title:str='f(x), f\'(x) and f\'\'(x)', 
        h:float=0.01
        ):
    
    x = np.linspace(x_start, x_end, x_count)
    plot_same(x, f(x), 'f(x)')	
    plot_same(x, f_derivative(x, f, h), 'f\'(x)')
    plot_same(x, f_2derivative(x, f, h), 'f\'\'(x)')
    plt.title(title)
    plt.legend()
    plt.show()