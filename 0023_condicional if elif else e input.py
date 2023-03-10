# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:10:33 2023

@author: El Pepe
"""

edad = int(input('¿Cuál es tu edad?\n'))

if edad <= 0:
     print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	 print('Eres menor de edad chamaco miado.')
elif edad > 18 and edad <= 45:
	 print('Eres mayor de edad pa.')
elif edad > 45 and edad <= 100:
	 print('Eres mayor de edad, pero ya no tan joven viejon.')
elif edad > 100 and edad <= 120:
	 print('Eres muy mayor viejo cochino.')
else:
	print('Edad no válida.')