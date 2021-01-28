# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:24:05 2020

@author: Martin
"""
import random
import numpy as np
import matplotlib.pyplot as plt
mu=1
s=1 
   
#Question 1 and 2
max_i=10
h=2**-max_i
N=1/h
t=np.arange(0,1+h,h)
W=np.zeros(int(N+1))
xh=np.ones(int(N+1))
x=np.ones(int(N+1))
eta=np.sqrt(h)*np.random.randn(int(N)) #the noise
for j in range(int(N)): #create W,xh and x for ith highest resolution
    W[j+1]=W[j]+eta[j]
    xh[j+1]=(1+h*mu)*xh[j]+s*xh[j]*(W[j+1]-W[j])
    x[j+1]=np.exp(((mu-s**2/2)*t[j+1])+s*W[j+1])    
plt.figure(1) #plot for Brownian motion
plt.plot(np.arange(0,1+h,h),W)
plt.figure(2) #plot for xh motion
plt.plot(np.arange(0,1+h,h),x)
plt.plot(np.arange(0,1+h,h),xh)

for i in range(max_i-1,0,-1): #create W,xh,x for all other i's
    h=2**-i
    N=1/h
    W=np.zeros(int(N+1))
    xh=np.ones(int(N+1))
    x=np.ones(int(N+1))
    eta_n=np.zeros(int(N))
    t_n=np.zeros(int(N+1))
    for j in range(int(N)): 
        eta_n[j]=eta[2*j]+eta[2*j+1]
        t_n[j+1]=t[2*(j+1)]
        W[j+1]=W[j]+eta_n[j]
        xh[j+1]=(1+h*mu)*xh[j]+s*xh[j]*(W[j+1]-W[j])
        x[j+1]=np.exp((mu-s**2/2)*t_n[j+1]+s*W[j+1]) 
    plt.figure(1) #plot for Brownian motion
    plt.plot(np.arange(0,1+h,h),W)
    plt.plot(np.arange(0,1+h,h),x)
    plt.figure(2) #plot for xh motion
    plt.plot(np.arange(0,1+h,h),xh)
    eta=eta_n
    t=t_n


plt.figure(1)
plt.savefig('Q1.pdf')
plt.figure(2)
plt.savefig('Q2.pdf')