from Funciones import descendig_selection
import random
'''Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.'''
#Ejercicio 1 Modificado:
number = int(input("Ingrese la cantidad de items que desea que tenga su lista: "))
new_list = []
for i in range(number):
    new_number = random.randint(1, 1000) #generamos números al azar
    new_list.append(new_number) #lo agregamos a la lista
print(f"La lista desordenada es: {new_list}")
definitive_list = descendig_selection(new_list) #lo ordenamos de manera descendente
print(f"La lista ordenada es: {definitive_list}")
