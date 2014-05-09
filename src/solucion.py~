#! /src/bin/python
#!encoding: UTF-8

import math
from sympy import *
  
def factorial(n):
   if n <= 1:
     return 1
   else:
     prod = n*factorial(n-1)
     return prod

def taylor(n,x,a):
  c = Symbol('c')
  funcion = sin(c)
  suma=funcion.evalf(subs={c:a})
  for i in range (1,n+1):
    derv = diff(funcion, c)
    termino = derv.evalf(subs={c:a})
    resultado = (termino/factorial(i))*((x-a)**i)
    suma = suma + resultado
    funcion = derv
    return taylor 
    
def error(n,x,a):
  c = Symbol('c')
  funcion = sin(c)
  f = funcion.evalf(subs={c: centro})
  suma = f
  for i in range (1,x + 1):
    derv = diff(f, c)
    termino = derv.evalf(subs={c: centro})
    resultado = (termino / factorial(i)) * ((x - a) ** i)
    suma = suma + resultado
    f = derv
  e = f - suma
  print 'El valor de la funcion original sin(%f) es igual a %f ' % (a, f)
  print 'El Polinomio de Taylor de grado n=%d en el punto centro c=%f evaluada en el punto x=%f es igual a %f' % (x, a, n, suma)
  print 'El Error de la funcion original con el Polinomio de Taylor es: error=%f' % e
  return error   

    
if __name__ == "__main__":
  n = int(raw_input("Introduzca el grado del polinomio:"))
  x = float(raw_input("Introduzca el punto donde se evalua el polinomio:"))
  a = float(raw_input("Introduzca el punto central donde se desea evaluar el polinomio:"))
  



