import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
from plotting import plot_same


def f_derivative(x, f, h=0.001):
    return (f(x+h) - f(x))/h

def f_2derivative(x, f, h=0.001):
    return (f_derivative(x+h, f, h) - f_derivative(x, f, h))/h



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