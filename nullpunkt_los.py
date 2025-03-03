from derivasjon_numerisk import f_derivative
from typing import Callable

def finn_med_newton_metoden(f:Callable[[float], float], x0:float, tol:float=1E-10, N:int=100):
    '''
    Finner nullpunktet til en funksjon f med Newtons metode.

    Parameters
    ---------- 
    f : callable
        Funksjonen vi skal finne nullpunktet til.
    fder : callable
        Den deriverte av funksjonen f.
    x0 : float
        Startgjett for nullpunktet.
    tol : float
        Toleransen for når vi skal stoppe iterasjonen.
    N : int
        Maksimalt antall iterasjoner.
    '''
    diff = abs(f(0))
    x = x0
    i = 0
    while diff > tol and i < N:
        x = x - f(x)/f_derivative(x, f)
        diff = abs(f(x))
        i += 1
    return x