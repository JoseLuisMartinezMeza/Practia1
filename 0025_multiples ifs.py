# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:42:46 2023

@author: El Pepe
"""

# Pedir al usuario que introduzca sus datos personales
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
ciudad = input("Introduce tu ciudad: ")
telefono = input("Introduce tu número de teléfono: ")
email = input("Introduce tu dirección de correo electrónico: ")
trabajo = input("¿En qué trabajas?: ")
hobby = input("¿Cuál es tu hobby favorito?: ")
mascota = input("¿Tienes mascota? (Sí/No): ")
deporte = input("¿Qué deporte te gusta practicar?: ")
comida = input("¿Cuál es tu comida favorita?: ")

# Utilizar condicionales if para mostrar un mensaje personalizado dependiendo de los datos introducidos por el usuario
if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
    
if ciudad == "Madrid":
    print("Vives en la capital de España.")
elif ciudad == "Barcelona":
    print("Vives en la segunda ciudad más grande de España.")
else:
    print(f"Vives en la ciudad de {ciudad}.")
    
if "@" in email:
    print("Tu dirección de correo electrónico es válida.")
else:
    print("Tu dirección de correo electrónico no es válida.")
    
if "informático" in trabajo:
    print("Trabajas en el campo de la informática.")
else:
    print(f"Trabajas como {trabajo}.")
    
if mascota.lower() == "sí":
    print("Tienes una mascota.")
else:
    print("No tienes mascota.")
    
if deporte.lower() == "fútbol":
    print("Te gusta el fútbol.")
else:
    print(f"Te gusta practicar {deporte}.")
    
if comida.lower() == "pizza":
    print("Tu comida favorita es la pizza.")
else:
    print(f"Tu comida favorita es {comida}.")
    
if "a" in nombre.lower():
    print("Tu nombre contiene la letra 'a'.")
else:
    print("Tu nombre no contiene la letra 'a'.")
    
if len(telefono) == 9:
    print("Tu número de teléfono es válido.")
else:
    print("Tu número de teléfono no es válido.")
    
if hobby.lower() == "viajar":
    print("Tu hobby favorito es viajar.")
else:
    print(f"Tu hobby favorito es {hobby}.")
