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
  inicio=time.time()
  c = Symbol('c')
  funcion = asin(c)
  suma=funcion.evalf(subs={c:a})
  for i in range (1,n+1):
    derv = diff(funcion, c)
    termino = derv.evalf(subs={c:a})
    resultado = (termino/factorial(i))*((x-a)**i)
    suma = suma + resultado
    funcion = derv
  fin=time.time()
  t=fin-inicio
  print 'Tiempo que tarda en sumar %f' %(t)
  return suma 
  
def error(n,x,a):
  inicio=time.time()
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
  fin=time.time()
  timp=fin-inicio
  print 'tiempo en calcular el error %f' %(timp)
  return error   

    
if __name__ == "__main__":
  n = int(raw_input("Introduzca el grado del polinomio:"))
  x = int(raw_input("Introduzca el punto donde se evalua el polinomio:"))
  a = float(raw_input("Introduzca el punto central donde se desea evaluar el polinomio:"))
  
suma = taylor(n,x,a)
print suma
error = error(n,x,a)
print error


