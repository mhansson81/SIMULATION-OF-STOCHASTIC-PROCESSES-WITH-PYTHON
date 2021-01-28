# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:16:37 2020

@author: Martin
"""

import random
import numpy as np
import matplotlib.pyplot as plt
mu=1
s=1 


#Question 1 - Plotting Brownian motion
max_i=10
h=2**-max_i
N=1/h
eta_0=np.sqrt(h)*np.random.randn(int(N))
W=np.zeros(int(N+1))
eta_0=np.sqrt(h)*np.random.randn(int(N))
eta=eta_0
for j in range(int(N)):
    W[j+1]=W[j]+eta[j]
plt.plot(np.arange(0,1+h,h),W)

for i in range(max_i-1,0,-1):
    h=2**-i
    N=1/h
    W=np.zeros(int(N+1))
    eta_n=np.zeros(int(N))
    for j in range(int(N)):
        eta_n[j]=eta[2*j]+eta[2*j+1]
        W[j+1]=W[j]+eta_n[j]
    plt.plot(np.arange(0,1+h,h),W)
    eta=eta_n
plt.savefig('Q1.pdf')


   
#Question 2
max_i=10
h=2**-max_i
N=1/h
t=np.arange(0,1+h,h)
W=np.zeros(int(N+1))
xh=np.ones(int(N+1))
x=np.ones(int(N+1))
eta=eta_0
for j in range(int(N)):
    W[j+1]=W[j]+eta[j]
    xh[j+1]=(1+h*mu)*xh[j]+s*xh[j]*(W[j+1]-W[j])
    x[j+1]=np.exp(((mu-s**2/2)*t[j+1])+s*W[j+1])    
plt.plot(np.arange(0,1+h,h),x)
plt.plot(np.arange(0,1+h,h),xh)

for i in range(max_i-1,0,-1):
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
    plt.plot(np.arange(0,1+h,h),x)
    plt.plot(np.arange(0,1+h,h),xh)
    eta=eta_n
    t=t_n
plt.savefig('Q2.pdf')


#Question 3
M=100
max_i=10
err=np.zeros(max_i)
for m in range(M):
    h=2**-max_i
    N=1/h
    t=np.arange(0,1+h,h)
    W=np.zeros(int(N+1))
    xh=np.ones(int(N+1))
    x=np.ones(int(N+1))
    eta=np.sqrt(h)*np.random.randn(int(N))
    for j in range(int(N)):
        W[j+1]=W[j]+eta[j]
        xh[j+1]=(1+h*mu)*xh[j]+s*xh[j]*(W[j+1]-W[j])
        x[j+1]=np.exp(((mu-s**2/2)*t[j+1])+s*W[j+1])    
    err[0]=err[0]+(x[j+1]-xh[j+1])**2
    for i in range(max_i-1,0,-1):
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
        err[max_i-i]=err[max_i-i]+(x[j+1]-xh[j+1])**2     
        eta=eta_n
        t=t_n
err=np.sqrt(err/M)
step=np.zeros(max_i)
for i in range(max_i):
    step[i]=2**-(max_i-i)
plt.loglog(step,err)
plt.loglog(step,np.sqrt(step))
plt.savefig('Q3_100.pdf')



#Question 4
M=100000
max_i=10
err=np.zeros(max_i)
for m in range(M):
    h=2**-max_i
    N=1/h
    t=np.arange(0,1+h,h)
    W=np.zeros(int(N+1))
    xh=np.ones(int(N+1))
    x=np.ones(int(N+1))
    eta=np.sqrt(h)*np.random.randn(int(N))
    for j in range(int(N)):
        W[j+1]=W[j]+eta[j]
        xh[j+1]=(1+h*mu)*xh[j]+s*xh[j]*(W[j+1]-W[j])
        x[j+1]=np.exp(((mu-s**2/2)*t[j+1])+s*W[j+1])    
    E[0]+=xh[j+1]
    for i in range(max_i-1,0,-1):
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
        E[max_i-i]+=xh[j+1] 
        eta=eta_n
        t=t_n
E=E/M
err=np.abs(np.exp(mu)-E)
step=np.zeros(max_i)
for i in range(max_i):
    step[i]=2**-(max_i-i)
plt.loglog(step,err)
plt.loglog(step,step)
plt.savefig('Q4_100000.pdf')


#Question 5
M=200000
max_i=10
E=np.zeros(max_i)
for m in range(M):
    h=2**-max_i
    N=1/h
    t=np.arange(0,1+h,h)
    W=np.zeros(int(N+1))
    xh=np.ones(int(N+1))
    x=np.ones(int(N+1))
    eta=np.sqrt(h)*np.random.randn(int(N))
    for j in range(int(N)):
        W[j+1]=W[j]+eta[j]
        xh[j+1]=(1+h*mu)*xh[j]+s*xh[j]*(W[j+1]-W[j])
        x[j+1]=np.exp(((mu-s**2/2)*t[j+1])+s*W[j+1])    
    E[0]+=xh[j+1]**2
    for i in range(max_i-1,0,-1):
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
        E[max_i-i]+=xh[j+1]**2
        eta=eta_n
        t=t_n
E=E/M
err=np.abs(np.exp(2*mu)-E)
step=np.zeros(max_i)
for i in range(max_i):
    step[i]=2**-(max_i-i)
plt.loglog(step,err)
plt.loglog(step,step)



     