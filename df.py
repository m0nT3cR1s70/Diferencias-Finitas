"""
    @author Define las aproximaciones
    de diferencias finitas
"""
import numpy as np

def fx(ux,x):
    """ Evalua una expresion en formato tipo python.
    Args:
        ux: 
            Cadena con formato numerico python.
        x: 
              Numero o arreglo donde se desea evaluar la función. 
    Returns:
            Devuele la evaluacion de la expresion exp.
.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""
    return eval(ux)

def forward(ux,x,h):
    """  Utiliza la aproximación de diferencias finitas
         para calcular la primera derivada de exp.
    Args:
        ux: 
            Expresion python.
        x: 
            Punto de evaluación de la derivada.
        h: 
            distancia entre punto y punto.
    Returns:
        Devuelve la aproximacion de la funcion con 
        la formula de diferencias finitas hacia adelante.
    """
    uh = ux.replace('x','(x+h)')
    return (eval(uh) - eval(ux))/h

def backforward(ux,x,h):
    """  Utiliza la aproximación de diferencias finitas
         para calcular la primera derivada de exp.
    Args:
        ux: 
            Expresion python.
        x: 
            Punto de evaluación de la derivada.
        h: 
            distancia entre punto y punto.
    Returns:
        Devuelve la aproximacion de la funcion con 
        la formula de diferencias finitas hacia adelante.
    """
    uh = ux.replace('x','(x-h)')
    return (eval(ux) - eval(uh))/h

def center(ux,x,h):
    """  Utiliza la aproximación de diferencias finitas
         para calcular la primera derivada de exp.
    Args:
        ux: 
            Expresion python.
        x: 
            Punto de evaluación de la derivada.
        h: 
            distancia entre punto y punto.
    Returns:
        Devuelve la aproximacion de la funcion con 
        la formula de diferencias finitas hacia adelante.
    """
    c1 = ux.replace("x","(x+h)")
    c2 = ux.replace("x","(x-h)")
    u = "1/2*("+ c1 + "-" + c2 + ")/h"
    return eval(u)

def d3(ux,x,h):
    """  Utiliza la aproximación de diferencias finitas
         para calcular la primera derivada de exp.
    Args:
        ux: 
            Expresion python.
        x: 
            Punto de evaluación de la derivada.
        h: 
            distancia entre punto y punto.
    Returns:
        Devuelve la aproximacion de la funcion con 
        la formula de diferencias finitas hacia adelante.
    """
    uh1 = ux.replace('x','(x+h)')
    uh2 = ux.replace('x','(x-h)')
    uh3 = ux.replace('x','(x-2*h)')
    u = "1/6*(2*" + uh1 + "+3*"+ ux + "-6*" + uh2 + "+" + uh3+ ")/h"
    return eval(u)

def d31(ux,x,h):
    """  Utiliza la aproximación de diferencias finitas
         para calcular la primera derivada de exp.
    Args:
        ux: 
            Expresion python.
        x: 
            Punto de evaluación de la derivada.
        h: 
            distancia entre punto y punto.
    Returns:
        Devuelve la aproximacion de la funcion con 
        la formula de diferencias finitas hacia adelante.
    """
    uh1 = ux.replace('x','(x+2*h)')
    uh2 = ux.replace('x','(x+h)')
    uh3 = ux.replace('x','(x-h)')
    u = "1/6*(-" + uh1 + "+6*"+ uh2 + "-3*" + ux + "-2*" + uh3+ ")/h"
    return eval(u)




def showAprox(h,fd,bd,cr,dl,dh):
    print("APROXIMACIONES")
    print("h\tforward\tbackforward\tcenter\ttrespuntos\ttrespuntos")
    for i in range(0,len(h)):
        print(h[i],"\t",fd[i],"\t",bd[i],"\t",cr[i],"\t",dl[i],"\t",dh[i])