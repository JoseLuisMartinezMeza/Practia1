# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:03:52 2023

@author: El Pepe
"""

x = 0

while x < 30:
    x += 1
    if x == 15:
        break
    if x in [4, 6, 10]:
        print('Se saltó el valor', x, 'de x')
        continue
    print('El valor del bucle es:', x)

print('Se rompió la ejecución del bucle cuando x valía', x)