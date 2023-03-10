# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:38:09 2023

@author: El Pepe
"""

# Definir la tupla con cuatro colores de elección
colores = ('rojo', 'verde', 'azul', 'amarillo')

# Solicitar al usuario que introduzca un color
color = input("Introduce un color: ")

# Comprobar si el color está en la tupla usando el operador in
if color in colores:
    # Si el color está en la tupla, imprimir un mensaje indicando que está admitido
    print(f"El color {color} está admitido")
else:
    # Si el color no está en la tupla, imprimir un mensaje indicando que no está admitido
    print("Color no admitido")
