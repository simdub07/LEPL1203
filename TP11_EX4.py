# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:01:57 2021

@author: simon du bois
"""

import numpy as np
import matplotlib.pyplot as plt

def evolT(V0):
    E = 0.3*V0
    h = 6.626e-34
    Hbar =  h/(2*np.pi)
    m = 9.109e-31
    
    return lambda a : 4*E*(V0-E)/(4*E*(V0-E)+V0**2*(np.sinh(a/Hbar *np.sqrt(2*m*(V0-E))))**2)

a = np.linspace(0.3,2)*1e-9
eV = 1.602e-19
T1 = evolT(eV)(a)
#plots 
plt.yscale('log')
plt.plot(a,T1,label = ("coefficient de transmission pour V0 = 1eV"), color="red")
plt.legend()
plt.title("Evolution du coefficient de transmission en fonction \n de la largeur de la barrière de potentiel")
plt.xlabel("Largeur de la barrière [nm]")
plt.ylabel("Coefficient de transmission (échelle logarithmique)")
plt.grid()
#ajout des points tout les 0.2 nm
plt.scatter(np.arange(0.4,2.2,0.2)*1e-9, evolT(eV)(np.arange(0.4,2.2,0.2)*1e-9), color = 'red')
plt.show()



