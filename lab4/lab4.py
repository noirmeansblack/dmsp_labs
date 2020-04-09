#!/usr/bin/env python
#coding=utf8

import matplotlib.pyplot as plt
import numpy as np
from numpy import exp,sqrt
n=10;m=100;ib=3;way=[];a=0
#X=np.random.uniform(a,m,n)
#Y=np.random.uniform(a,m,n)

with open('data.txt', 'r') as f:
    XY = [[int(num) for num in line.split(',')] for line in f]
X = XY[0]
Y = XY[1]

#X=[10, 10, 100,100 ,30, 20, 20, 50, 50, 85, 85, 75, 35, 25, 30, 47, 50]
#Y=[5, 85, 0,90,50, 55,50,75 ,25,50,20,80,25,70,10,50,100]
#n=len(X)
M = np.zeros([n,n])
for i in np.arange(0,n,1):
         for j in np.arange(0,n,1):
                  if i!=j:
                           M[i,j]=sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2)
                  else:
                           M[i,j]=float('inf')
way.append(ib)
for i in np.arange(1,n,1):
         s=[]
         for j in np.arange(0,n,1):
                  s.append(M[way[i-1],j])
         way.append(s.index(min(s)))
         for j in np.arange(0,i,1):
                  M[way[i],way[j]]=float('inf')
                  M[way[i],way[j]]=float('inf')
S=sum([sqrt((X[way[i]]-X[way[i+1]])**2+(Y[way[i]]-Y[way[i+1]])**2) for i in np.arange(0,n-1,1)])+ sqrt((X[way[n-1]]-X[way[0]])**2+(Y[way[n-1]]-Y[way[0]])**2)
plt.title('загальний шлях: %s.номер міста: %i.всього міст: %i.'%(round(S,3),ib,n), size=14)
X1=[X[way[i]] for i in np.arange(0,n,1)]
Y1=[Y[way[i]] for i in np.arange(0,n,1)]
plt.plot(X1, Y1, color='g', linestyle=' ', marker='o')
plt.plot(X1, Y1, color='b', linewidth=1)
X2=[X[way[n-1]],X[way[0]]]
Y2=[Y[way[n-1]],Y[way[0]]]
plt.plot(X2, Y2, color='r', linewidth=2,  linestyle='-', label='шлях між першим і \n останнім містами')
plt.legend(loc='best')
plt.grid(True)
plt.show()
