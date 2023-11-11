from funciones import pair
from funciones import odd
'''Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
•	1 es impar.
•	Si un número es impar, su antecesor es par; y viceversa.'''
number = int(input("Ingrese un número: "))
if pair(number):
    print("El número es par")
else:
    print("El número es impar")

#Por si queremos probar con la otra funcion
'''if odd(number):
    print("El número es impar")
else:
    print("El número es par")'''
