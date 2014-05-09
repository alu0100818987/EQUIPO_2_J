#! /src/bin/python
#!encoding: UTF-8

import math
from sympy import *
import time
  
def factorial(n):
   if n <= 1:
     return 1
   else:
     prod = n*factorial(n-1) 
     return prod

def taylor(n,x,a):
  c = Symbol('c')
  funcion = asin(c)
  suma=funcion.evalf(subs={c:a})
  for i in range (1,n+1):
    derv = diff(funcion, c)
    termino = derv.evalf(subs={c:a})
    resultado = (termino/factorial(i))*((x-a)**i)
    suma = suma + resultado
    funcion = derv
  return suma 
  
def error(n,x,a):
  c = Symbol('c')
  funcion = asin(c)
  f= funcion.evalf(subs={c:a})
  fun = funcion.evalf(subs={c:a})
  suma = funcion.evalf(subs={c:a})
  for i in range (1,x + 1):
    derv = diff(funcion, c)
    termino = derv.evalf(subs={c:a})
    resultado = (termino / factorial(i)) * ((x - a) ** i)
    suma = suma + resultado
    f = derv
  error = fun - suma
  return error   

    
if __name__ == "__main__":
  
  n = int(raw_input("Introduzca el grado del polinomio:"))
  x = int(raw_input("Introduzca el punto donde se evalua el polinomio:"))
  a = float(raw_input("Introduzca el punto central donde se desea evaluar el polinomio:"))
  if (abs(a)>1)or(abs(x)>1):
    print 'Debe introducir valores de a entre [-1,1]'
    a = float(raw_input("Introduzca el punto central donde se desea evaluar el polinomio:"))
    x = int(raw_input("Introduzca el punto donde se evalua el polinomio:"))
    
start=time.time()
suma = taylor(n,x,a)
finish=time.time()-start
error = error(n,x,a)
e=abs(error)
print 'Valor de la aproximacion'
print suma
print 'Valor del error'
print e
print 'Tiempo que tarda el programa en ejecutarse'
print finish


