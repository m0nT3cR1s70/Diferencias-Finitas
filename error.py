# -*- coding: utf-8 -*-
import numpy as np

def absoluto(aprox,exac):
    """ Calcula el error de aproximacion.
    Args:
        aprox: 
            Aproximacion obtenida por medio de diferencias finitas.
        exac: 
            Valor exacto de la derivada. 
    Returns:
            Devuele lel error entre el valor aproximado y el exacto.
.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""
    return abs(aprox-exac)


def rms(aprox,exac):
    """ Calcula el error de aproximacion.
    Args:
        aprox: 
            Aproximacion obtenida por medio de diferencias finitas.
        exac: 
            Valor exacto de la derivada. 
    Returns:
            Devuele lel error entre el valor aproximado y el exacto.
.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""
    er = ((exac-aprox)**2)*(1/len(aprox))
    return np.sqrt(er)




def showError(h,ef,eu,ec,ed,ed1):
    """
        Muestra en pantalla una tabla, con los principales errores 
        de las diferentes aproximaciones utilizadas por diferencias
        finitas.
    """
    print("Errores en diferentes aproximaciones en diferencias finitas\n\n")
    print("h\tD+u\tD-u\tD0\tD1\tD2")
    for i in range(0,len(ef)):
        print(h[i],"\t",ef[i],"\t",eu[i],"\t",ec[i],"\t",ed[i],"\t",ed1[i])

