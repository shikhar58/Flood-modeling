# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 23:52:53 2023

@author: shikh
"""


import numpy as np

length=1000
time=3600

sizex=20
sizet=2

hint=1
hinf=2
houtf=1

vint=1
voutf=1
vinf=2


h=np.zeros((int(time/sizet),int(length/sizex)))


v=np.zeros((int(time/sizet),int(length/sizex),))

h[0,:] = hint


h[:,0]=hinf

h[:,-1]=houtf



v[0,:] = vint

v[:,0]=vinf

v[:,-1]=voutf


rat=sizet/sizex


for i in range(0,int(time/sizet)-1):
    for j in range(1,int(length/sizex)-1):
        h[i+1,j]=h[i,j]+rat*(h[i,j-1]*v[i,j-1]-h[i,j]*v[i,j])
        v[i+1,j]=h[i,j]+rat*(v[i,j]*(v[i,j-1]-v[i,j])+9.8*(h[i,j-1]-h[i,j]))
        print("x and t are",j,i)
        
        
import matplotlib.pyplot as plt

fig=plt.figure()

plt.plot(range(len(v[:,0])),v[:,40])
plt.show()

st.pyplot(fig)

plt.plot(range(len(h[:,0])),h[:,40])



st.pyplot(fig)
