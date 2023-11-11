'''Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.'''
from funciones import is_power
print("Ingrese dos números para saber si son potencia ---->")
number_1 = int(input("Ingrese el primer número: "))
number_2 = int(input("Ingrese el segundo número: "))
result = is_power(number_1, number_2)
if result == True:
    print(f"{number_1} es potencia de {number_2}")
else:
    print(f"{number_1} NO es potencia de {number_2}")
