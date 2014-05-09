#!/src/bin/python

import math
from sympy import *

def factorial(numero):
  factorial = 1
  while(numero > 1):
    factorial = factorial * numero
    numero = numero - 1
  return factorial
  
def taylor(x, numero, centro):
  c = Symbol('c')
  f = math.sin(c)
  suma = f.evalf(subs={c: centro})
  for i in range (1,numero + 1):
    #v=[i]

    #k=(x-c)**i
    print 'el polinomio de taylor de grado %d es:' % i
    if i==0:
      print'p=%f' % s
    else:
      print 'p = (%f)*((x-%f)**%d)' % (s,c,i)
    f_i = diff(f, c)
    v = f_i.evalf()
    s= (v / factorial(i)) * ((x - centro) ** i)
    suma = suma + v
    f = f_i
  return funcion