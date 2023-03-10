# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 17:22:39 2023

@author: El Pepe
"""



teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

    
del teclado1

# Eliminar las claves 'Categoría' y 'Precio' del diccionario teclado2
del teclado2['Categoría']
del teclado2['Precio']

# Mostrar la última clave que queda en el diccionario teclado2
for x in teclado2:
	print(x, '=', teclado2[x] + '.')