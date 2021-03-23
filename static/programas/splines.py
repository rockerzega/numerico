# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 19:43:45 2021

@author: Luis Vaquilema
"""

import numpy as np
from scipy.interpolate import CubicHermiteSpline
import matplotlib.pyplot as plt

def Hermite (x,y,dydx):
    li=x[0]-0.5
    ls=(x[len(x)-1])+0.5
    cs = CubicHermiteSpline(x, y, dydx)
    xs=np.arange(li,ls,0.1)
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(x, y, 'o', label='puntos')
    ax.plot(xs, cs(xs), label="Spline")
    ax.set_xlim(li, ls)
    
    ax.legend(loc='lower left', ncol=2)
    plt.savefig('hermite.jpg')
    #plt.show()



def polinomio(x,y,dydx):
    A0=y[0]
    A1=dydx[0]
    h=x[1]-x[0]
    z1=(y[1]-y[0])/h
    z2=(z1-dydx[0])/h
    A2=z2
    z3=(dydx[1]-z1)/h
    z4=(z3-z2)/h
    A3=z4
    
    P3=A3
    P2=A2-(A3*x[1])-(2*A3*x[0])
    P1=A1+(x[0]*((A3*x[0])+(2*A3*x[1])-(2*A2)))
    P0=A0+(x[0]*((A2*x[0])-A1-(A3*x[0]*x[1])))
    
    poli=''
    if(P3!=0):
        poli=str(round(P3,4))+'(x^3) '
    
    if(P2!=0.0):
        if(P2>0):
            poli+='+ '
        poli+=str(round(P2,4))+'(x^2) '
    
    if(P1!=0.0):
        if(P1>0):
            poli+='+ '
        poli+=str(round(P1,4))+'x '
    
    if(P0!=0.0):
        if(P0>0):
            poli+='+ '
        poli+=str(round(P0,4))
    
    return poli


def interpolacionHermite(lista):
    matriz=np.array(lista)
    x=matriz[0,:]
    y=matriz[1,:]
    dydx=matriz[2,:]
    Hermite(x, y, dydx)
    salida=[]
    for i in range(len(x)-1):
        salida.append('S('+str(i)+') = '+polinomio(x[i:i+2],y[i:i+2],dydx[i:i+2]))
    Hermite(x, y, dydx)
    return salida

lista=[
        [1, 2, 2.5, 4],
        [2, -1,0, 1],
        [0, 1, 1, -1]
        ]
#matriz=np.array(lista)
#x=matriz[0,:]
#y=matriz[1,:]
#dydx=matriz[2,:]

#Hermite(x, y, dydx)

#(poli, fig)=interpolacionHermite(lista)
#fig
#print(poli)



    
    


"""
x = np.arange(10)
print(x)
y = np.sin(x)
print(y)
cs = CubicSpline(x, y)
xs = np.arange(-0.5, 9.6, 0.1)
print(xs)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
ax.plot(xs, np.sin(xs), label='true')
ax.plot(xs, cs(xs), label="S")
ax.plot(xs, cs(xs, 1), label="S'")
ax.plot(xs, cs(xs, 2), label="S''")
ax.plot(xs, cs(xs, 3), label="S'''")
ax.set_xlim(-0.5, 9.5)
ax.legend(loc='lower left', ncol=2)
plt.show()
"""

