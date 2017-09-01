#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:12:57 2017

@author: m0nT3cR1s70
"""
import matplotlib.pyplot as plt


def graError(h,ef,eb,ec,e3,e4):
    plt.plot(h,ef,'b',label='forward')
    plt.plot(h,eb,'g',label='backforward')
    plt.plot(h,ec,'r',label='center')
    plt.plot(h,e3,'k',label='tres puntos ba')
    plt.plot(h,e4,'m',label='tres puntos fo')
    plt.xlabel("log(h)")
    plt.ylabel("log(ux)")
    plt.legend()
    plt.loglog()
    plt.grid()
    plt.show()

def grafic(rho1,rho2,rho3,x1,x2,x3,d1,d2,d3):
    plt.subplot(311)
    plt.plot(x1,rho1,'o-')
    plt.plot(x1,d1,label='Malla 10 nodos')
    plt.legend()
    plt.subplot(312)
    plt.plot(x2,rho2,'o-')
    plt.plot(x2,d2,label='Malla 20 nodos')
    plt.legend()
    plt.subplot(313)
    plt.plot(x3,rho3,'o-')
    plt.plot(x3,d3,label='Malla 100 nodos')
    plt.subplots_adjust(hspace=0.5)
    plt.legend()
    plt.show()


