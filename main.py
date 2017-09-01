#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    @author: m0nT3cR1s70
    @version: 1.0
    @brief: EJERCICIO 6, TAREA 1 MMCST20181
"""

#Librerias utiles
import numpy as np
import df
import error
import grafica

###############################################################################
# INCISO A
# Se define las entradas necesarias
ux = "np.sin(x)" # Funcion a aproximar su derivada
du = "np.cos(x)" # Derivada exacta de f para comparar el error
#ux = "x**2+3"
#du = "2*x"
h = np.zeros(5)
h[0] = 0.1
h[1] = 0.05
h[2] = 0.01
h[3] = 0.005
h[4] = 0.001
#h = [0.1,0.05,0.01,0.005,0.001] # Definimos los h, donde se busca la solucion
#x = 1.0 # Punto en donde se desea la derivada
x = np.ones(5)
#Calculamos las aproximacion a u'(x)
fw = df.forward(ux,x,h)       # Diferencias hacia adelante
bf = df.backforward(ux,x,h)   # Diferencias hacia atras
ct = df.center(ux,x,h)        # Diferencias centradas
dl = df.d3(ux,x,h)            # Diferencias con tres puntos
dh = df.d31(ux,x,h)           # Diferencias con tres puntos
# Mostramos los datos en pantalla
df.showAprox(h,fw,bf,ct,dl,dh)
###############################################################################
#INCISCO B
# Calcular el error de truncamiento y graficarlo
#Evaluamos la derivada exacta de f
dx = df.fx(du,x)
# Calculamos el error entre las aproximaciones
ef = error.error(fw,dx) # diferencias hacia adelante
eb = error.error(bf,dx) # diferencias hacia atras
ec = error.error(ct,dx) # diferencias centradas
e3 = error.error(dl,dx) # diferencias con tres puntos
e4 = error.error(dh,dx) # diferencias con tres puntos
# Graficamos el error obtenido
grafica.graError(h,ef,eb,ec,e3,e4)
################################################################################
#INCISCO C
A  =  0  # extremo izquiero de la varilla
B  = 10  # extremo derecho de la varilla
n1 = 10  # Numero de nodos en la primera malla
n2 = 20  # Numero de nodos en la segunda malla
n3 = 100 # Numero de nodos en la tercera malla
mx = "(2*x**3+4*x**2)" # masa
rho= "6*x**2+8*x"      # densidad
x1 = np.linspace(A,B,n1)  # Malla 1
x2 = np.linspace(A,B,n2)  # Malla 2
x3 = np.linspace(A,B,n3) # Malla 3
h1 = (B-A)/(n1-1)      #h para la primera malla
h2 = (B-A)/(n2-1)      #h para la segunda malla
h3 = (B-A)/(n3-1)      #h para la tercera malla
# Calculo exacto de la densidad
rho1 = df.fx(rho,x1)
rho2 = df.fx(rho,x2)
rho3 = df.fx(rho,x3)
# Calculamos las aproximaciones con forward
fw1 = df.forward(mx,x1,h1)
fw2 = df.forward(mx,x2,h2)
fw3 = df.forward(mx,x3,h3)
# Graficamos la distribucion de densidad
#grafica.grafic(rho1,rho2,rho3,x1,x2,x3,fw1,fw2,fw3)
# Calculamos las aproximaciones con backforward
bfw1 = df.backforward(mx,x1,h1)
bfw2 = df.backforward(mx,x2,h2)
bfw3 = df.backforward(mx,x3,h3)
# Calculamos las aproximaciones con diferencias centradas
cr1 = df.center(mx,x1,h1)
cr2 = df.center(mx,x2,h2)
cr3 = df.center(mx,x3,h3)
# Calculamos las aproximaciones con diferencias con tres puntod
d11 = df.d31(mx,x1,h1)
d21 = df.d31(mx,x2,h2)
d31 = df.d31(mx,x3,h3)
# Calculamos las aproximaciones con diferencias con tres puntod
d1 = df.d3(mx,x1,h1)
d2 = df.d3(mx,x2,h2)
d3 = df.d3(mx,x3,h3)
###############################################################################
#INCISO D
ef1 = error.rms(fw1,rho1)

