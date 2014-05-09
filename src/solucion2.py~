#! encoding: utf8
# Ya puedo usar el español

import matplotlib.pylab as pl 
import numpy as np
import math

x=int(raw_input('kjzdb: '))
h=int(raw_input('kjzdb: '))
l=[]
for i in range (x):
  y=1/np.sin(x)
  l.append(y)
  
pl.figure(figsize=(8,6), dpi=80)

pl.subplot(1,1,1)

X = np.linspace(-x, x, 256, endpoint=True)
C = 0*(X)
S = 1/np.sin(X)

pl.plot(X,C, color="black", linewidth=1.0, linestyle="-", label="Eje de las X")
pl.plot(X,S, color="yellow", linewidth=1.5, linestyle="-", label="arcoseno")

pl.legend(loc='upper left')

#pl.xlim(-4.0,4.0)
pl.xlim(X.min()*1.1,X.max()*1.1)

#pl.xticks(np.linspace(-4,4,9,endpoint=True))
pl.xticks([-x, x])

#pl.ylim(-1.0,1.0)
pl.ylim(C.min()*1.1,C.max()*1.1)

#pl.yticks(np.linspace(-1,1,5,endpoint=True))
pl.yticks([-h, h])

pl.title("Representacion grafica")

pl.savefig("sencos.eps", dpi=72)

pl.show()
