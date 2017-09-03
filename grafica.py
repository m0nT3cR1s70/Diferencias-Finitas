#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:12:57 2017

@author: m0nT3cR1s70
"""
import matplotlib.pyplot as plt


def graError(h,ef,eb,ec,e3,e4):
    plt.figure()
    plt.plot(h,ef,'b',label='$D_{{+}}$')
    plt.plot(h,eb,'g',label='$D_{{-}}$')
    plt.plot(h,ec,'r',label='$D_{{0}}$')
    plt.plot(h,e3,'k',label='$D_{{3}}$')
    plt.plot(h,e4,'m',label='$D_{{-3}}$')
    plt.xlabel("log(h)")
    plt.ylabel("log(ux)")
    plt.legend()
    plt.loglog()
    plt.grid()
    plt.show()

def grafic(rho1,rho2,rho3,x1,x2,x3,d1,d2,d3,title):
    plt.figure()
    plt.subplot(311)
    plt.title(title)
    plt.plot(x1,rho1,'o-')
    plt.plot(x1,d1,label='Malla 10 nodos')
    plt.grid()
    plt.legend()
    plt.subplot(312)
    plt.plot(x2,rho2,'o-')
    plt.plot(x2,d2,label='Malla 20 nodos')
    plt.grid()
    plt.legend()
    plt.subplot(313)
    plt.plot(x3,rho3,'o-')
    plt.plot(x3,d3,label='Malla 100 nodos')
    plt.grid()
    plt.subplots_adjust(hspace=0.5)
    plt.legend()
    plt.show()


