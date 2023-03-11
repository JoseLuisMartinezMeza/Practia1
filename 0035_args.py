# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:33:09 2023

@author: El Pepe
"""
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')



def colores2(*args):
    if len(args) < 2:
        print("Se necesitan al menos dos argumentos.")
    else:
        print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores2('rojo', 'azul') # El color azul es mi favorito. El color rojo tampoco está mal.

def suma(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    print("El resultado de la suma es:", resultado)

suma(2, 3, 5, 7, 11) # El resultado de la suma es: 28