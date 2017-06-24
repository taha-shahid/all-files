from sympy import*
from sympy.solvers.diophantine import diophantine
x, y, z= symbols("x, y, z", integer=True)
diophantine(6*x+9*y+20*z-50)
