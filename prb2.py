# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:39:31 2020

@author: ASUS
"""
import numpy as np
import matplotlib.pyplot as plt
l=10
dx=2
nx=int(l/dx)+1
x=np.linspace(0,l,nx)

t=12
dt=0.1
nt=int(t/dt)
rho=2.7
cp=0.2174
lamda=0.020875
T1=0
T=np.ones(nx)*T1


for n in range(0,nt):
    
        
    Tn=T.copy()
    T[1:-1]=Tn[1:-1]+lamda*(Tn[2:]-2*Tn[1:-1]+Tn[0:-2])
    T[0]=100
    T[-1]=50
    
plt.plot(x,T)
plt.show ()



