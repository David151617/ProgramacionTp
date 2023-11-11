from Funciones import ascendig_selection
from Funciones import descendig_selection
'''Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.'''
#Lista con letras al azar
list_1 = ["A", "B", "X", "C", "R", "M", "D"]
print(f"Desordenada: {list_1}")
list_1 = ascendig_selection(list_1) #Lo ordena de manera ascendente
print(f"Ascendente: {list_1}")
list_1 = descendig_selection(list_1) #Lo ordena de manera descendente
print(f"Descendente: {list_1}")