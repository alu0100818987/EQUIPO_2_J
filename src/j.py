#! /usr/bin/python

import math
from sympy import *

c = Symbol('c')
funcion = asin(c)

def taylor(n,x,a):
  suma=funcion.evalf(subs={c:a})

if __name__ == "__main__":
  n = int(raw_input("Introduzaca el grado del polinomio:"))
  x = float(raw_input("Introduzca el punto donde se evalua el polinomio:"))
  a = float(raw_input("Introduzca el punto central donde se desea evaluar el polinomio:"))
  
print suma