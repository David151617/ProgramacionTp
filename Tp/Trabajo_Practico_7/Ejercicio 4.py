from Funciones import insertion_sort
'''Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud.
Puedes utilizar el método de ordenamiento de inserción.'''
#lista de palabras al azar
list_1 = ["Programación", "Elefante", "Campeones", "Arreglo", "Ordenamiento"]
print("La lista sin orden es: ",list_1) 
list_1 = insertion_sort(list_1) #ordenamos por inserción
print("La lista ordenada por longitud es: ",list_1)
