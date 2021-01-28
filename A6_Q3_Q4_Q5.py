# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:15:48 2020

@author: Martin
"""
import random
import numpy as np
import matplotlib.pyplot as plt
mu=1
s=1
a=1
#Question 3-5
M=10000
max_i=7
err_s=np.zeros(max_i) #vector for strong error
E1=np.zeros(max_i) #vector for E in when phi=X
E2=np.zeros(max_i) #vector for E in when phi=X^2
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
    err_s+=(x[j+1]-xh[j+1])**2
    E1[0]+=xh[j+1]
    E2[0]+=xh[j+1]**2
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
        err_s[max_i-i]+=(x[j+1]-xh[j+1])**2 #sum for strong error 
        E1[max_i-i]+=xh[j+1] #sum for weak error phi=X
        E2[max_i-i]+=xh[j+1]**2 #sum for weak error with phi=X^2
        eta=eta_n #renew eta with doubled increment
        t=t_n #renew eta with doubled increment
err_s=np.sqrt(err_s/M)
err_w1=np.abs(np.exp(mu)-E1/M)
err_w2=np.abs(np.exp(2*mu+a*s)-E2/M)

step=np.zeros(max_i)
for i in range(max_i):
    step[i]=2**-(max_i-i)

plt.figure(3) #plot strong error
plt.loglog(step,err_s)
plt.loglog(step,np.sqrt(step))
plt.savefig('Q3.pdf')

plt.figure(4) #plot weak error phi=X
plt.loglog(step,err_w1)
plt.loglog(step,step)
plt.savefig('Q4.pdf')

plt.figure(5) #sum for weak error with phi=X
plt.loglog(step,err_w2)
plt.loglog(step,step)
plt.savefig('Q5.pdf')


