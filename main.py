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
h   = np.array([0.1,0.005,0.01,0.005,0.001])  # array de numpy 
x = 1.0 # Punto en donde se desea la derivada 
# Se aproxima y se almacena en un arreglo a u'(x) para cada h.  
fw = df.forward(ux,x,h)       # Diferencias hacia adelante
bf = df.backforward(ux,x,h)   # Diferencias hacia atras
ct = df.center(ux,x,h)        # Diferencias centradas
dl = df.d3(ux,x,h)            # Diferencias conjunto 1
dh = df.d31(ux,x,h)           # Diferencias conjunto 2
# Mostramos los datos en pantalla
df.showAprox(h,fw,bf,ct,dl,dh)
###############################################################################
#INCISCO B
# Calcular el error de truncamiento y graficarlo.
#Evaluamos la derivada exacta de f
dx = df.fx(du,x)  
# Calculamos el error entre las aproximaciones
ef = error.absoluto(fw,dx) # diferencias hacia adelante
eb = error.absoluto(bf,dx) # diferencias hacia atras
ec = error.absoluto(ct,dx) # diferencias centradas
e3 = error.absoluto(dl,dx) # diferencias con cuatro puntos
e4 = error.absoluto(dh,dx) # diferencias con cuatro puntos
# Graficamos el error obtenido
grafica.graError(h,ef,eb,ec,e3,e4)
################################################################################
#INCISCO C
A  =  0  # extremo izquiero de la varilla
B  = 10  # extremo derecho de la varilla
n  = [10,20,100]
masa = "(2*x**3+4*x**2)" # masa
densidad  = "6*x**2+8*x"      # densidad
x1 = np.linspace(A,B,n[0])  # Malla 1
x2 = np.linspace(A,B,n[1])  # Malla 2
x3 = np.linspace(A,B,n[2])  # Malla 3
h1 = (B-A)/(n[0]-1)      #h para la primera malla
h2 = (B-A)/(n[1]-1)      #h para la segunda malla
h3 = (B-A)/(n[2]-1)      #h para la tercera malla
# Calculo exacto de la densidad
rho1 = df.fx(densidad,x1)
rho2 = df.fx(densidad,x2)  
rho3 = df.fx(densidad,x3)  
# Calculamos y graficamos las aproximaciones con forward
fw1 = df.forward(masa,x1,h1)
fw2 = df.forward(masa,x2,h2)
fw3 = df.forward(masa,x3,h3)
title = 'Aproximación $D_{{+}}u(x)$'
grafica.grafic(rho1,rho2,rho3,x1,x2,x3,fw1,fw2,fw3,title)
# Calculamos y graficamos las aproximaciones con backforward
bfw1 = df.backforward(masa,x1,h1)
bfw2 = df.backforward(masa,x2,h2)
bfw3 = df.backforward(masa,x3,h3)
title = 'Aproximación $D_{{-}}u(x)$'
grafica.grafic(rho1,rho2,rho3,x1,x2,x3,bfw1,bfw2,bfw3,title)
# Calculamos y graficamos las aproximaciones con diferencias centradas
cr1 = df.center(masa,x1,h1)
cr2 = df.center(masa,x2,h2)
cr3 = df.center(masa,x3,h3)
title = 'Aproximación $D_{{0}}u(x)$'
grafica.grafic(rho1,rho2,rho3,x1,x2,x3,cr1,cr2,cr3,title)
# Calculamos y graficamos las aproximaciones con diferencias con c1
d11 = df.d31(masa,x1,h1)
d21 = df.d31(masa,x2,h2)
d31 = df.d31(masa,x3,h3)
title = 'Aproximación $D_{{3}}u(x)$'
grafica.grafic(rho1,rho2,rho3,x1,x2,x3,d11,d21,d31,title)
# Calculamos y graficamos las aproximaciones con diferencias con c2
d1 = df.d3(masa,x1,h1)
d2 = df.d3(masa,x2,h2)
d3 = df.d3(masa,x3,h3)
title = 'Aproximación $D_{{-3}}u(x)$'
grafica.grafic(rho1,rho2,rho3,x1,x2,x3,d1,d2,d3,title)
###############################################################################
#INCISO D
ef1 = error.rms(fw1,rho1)
ef2 = error.rms(fw2,rho2)

