import matplotlib.pyplot as plt
import numpy as np

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

def plot_same_from_start_end(f, x_start, x_end, x_count, title="f(x)", min_x=None, max_x=None, min_y=None, max_y=None):
    x, y = generate_x_y(f, x_start, x_end, x_count)
    plot_same(x, y, title, min_x, max_x, min_y, max_y)

def generate_x_y(f, x_start, x_end, x_count):
    x = np.linspace(x_start, x_end, x_count)
    y = f(x)
    return x, y