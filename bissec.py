## do wesley   x**3-9*x+3    10**-4

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.plotting import *

import sympy

raiz = []
funStr = input("Digite a função: \n")
epsStr = input("Digite o épsilon: \n")

x = sympy.Symbol('x')

funcao = eval(funStr)

plot(funcao,(x,-1000,1000))
def f(x):
  f = eval(funStr)
  return f
  
def bissec(f,a,b,tol,ite_max):
  aux = 1
  FA = f(a)
  FB = f(b)

  while aux < ite_max:
    p = (a+b)/2
    FP = f(p)
    if FP == 0 or (b-a)/2 < eval(tol):
      raiz.append(p)
      return 'A raiz a ser considerada é: ' + str(p)
    aux += 1
    if FA * FP > 0:
      a = p
      FA = FP
    else:
      b = p
  return 'O método falhou após ' + str(ite_max) + ' iterações'

bissec(f,1,2,epsStr,100)

print(raiz)

# plt.plot(raiz, f,'mo')