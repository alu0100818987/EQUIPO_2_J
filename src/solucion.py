#! /src/bin/python
#!encoding: UTF-8

import math
from sympy import *
import time
import matplotlib.pylab as pl 
import numpy as np


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



g=int(raw_input('Intervalo para el eje de las X: '))
h=int(raw_input('Intervalo para el eje de las Y: '))
l=[]
for i in range (x):
  y=1/np.sin(x)
  l.append(y)
  
pl.figure(figsize=(8,6), dpi=80)

pl.subplot(1,1,1)

X = np.linspace(-g, g, 256, endpoint=True)
C = 0*(X)
S = 1/np.sin(X)

pl.plot(X,C, color="black", linewidth=1.0, linestyle="-", label="Eje de las X")
pl.plot(X,S, color="yellow", linewidth=1.5, linestyle="-", label="arcoseno")

pl.legend(loc='upper left')

#pl.xlim(-4.0,4.0)
pl.xlim(X.min()*1.1,X.max()*1.1)

#pl.xticks(np.linspace(-4,4,9,endpoint=True))
pl.xticks([-g, g])

#pl.ylim(-1.0,1.0)
pl.ylim(C.min()*1.1,C.max()*1.1)

#pl.yticks(np.linspace(-1,1,5,endpoint=True))
pl.yticks([-h, h])

pl.title("Representacion grafica")

pl.savefig("sencos.eps", dpi=72)

pl.show()
