import random
from Funciones import bubble_sort
'''Escribe un programa que tome una lista de números como entrada y
la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.'''
#Pedimos al usuario que ingrese el tamaño de la lista
number = int(input("Ingrese la cantidad de items que desea que tenga su lista: "))
new_list = []
for i in range(number): #Recorremos el tamaño indicado
    new_number = random.randint(1, 1000) #Le asignamos valores al azar
    new_list.append(new_number) 
print(f"La lista desordenada es: {new_list}")
definitive_list = bubble_sort(new_list) #Ordenamos la lista original, y se la asignamos a la nueva
print(f"La lista ordenada es: {definitive_list}")