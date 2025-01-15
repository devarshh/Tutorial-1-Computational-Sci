import numpy as np

def Newton(f, df, x0, kMax, eps_x, eps_f):
    x = x0
    conv = False
    for i in range(kMax):
        r = f(x)
        dx = -r/df(x)
        x += dx
        err = abs(dx)
        res = abs(r)
        print('Iteration %d err=%e res%e x=%e.' %)
        if err < eps_x and res < eps_f:
            conv = True
            break
        return x, err, res, conv
    
    
def f(x):
    return x - np.cos(x)

def df(x):
    return 1 + np.sin(x)

x0 = 0.75
kMax = 5
eps_x = 1e-13
eps_f = 1e-13

x, err, res, conv = Newton(f, df, x0, kMax, eps_x, eps_f)
