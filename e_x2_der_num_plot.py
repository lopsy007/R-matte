import derivasjon_numerisk as plot
import math


f = lambda x: math.e**(-x**2)
plot.plot_same_with_derivatives(f, -3, 3,)

