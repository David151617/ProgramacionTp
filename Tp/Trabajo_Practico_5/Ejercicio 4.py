'''4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.'''

import sys
sys.path.append("C:/Users/David Amore/OneDrive/Escritorio/Repo_program/ProgramacionTp/Tp")
from Funcion_es import funciones
number_1 = int(input ("Ingrese el primer número entero: "))
number_2 = int(input("Ingrese el segundo número entero: "))
if number_1 > number_2:
    if funciones.multiple(number_1, number_2):
        print(f"{number_2} es múltiplo de {number_1}")
    else:
        print("Ninguno de los números son multiplos")
elif number_1 < number_2:
    if funciones.multiple(number_2, number_1):
        print(f"{number_1} es múltiplo de {number_2}")
    else:
        print("Ninguno de los números son multiplos")
else:
    print("Los números son iguales")    