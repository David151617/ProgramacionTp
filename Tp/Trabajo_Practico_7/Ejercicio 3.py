from Funciones import selction_dictionary
from Funciones import bubble_dictionary
'''Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). 
Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.'''
#Creamos una lista que contiene diccionarios
books = [
    {"titulo": "Libro A", "autor": "Autor X", "fecha": 2005},
    {"titulo": "Libro B", "autor": "Autor Y", "fecha": 2010},
    {"titulo": "Libro C", "autor": "Autor Z", "fecha": 2002},
    {"titulo": "Libro D", "autor": "Autor Y", "fecha": 2015},
]

# Pedimos al usuario que elija el campo por el cual ordenar
field_to_sort = input("Ingrese el campo por el cual desea ordenar (titulo, autor, fecha): ")

# Ordenamos con selección
list_selection_sort = selction_dictionary(books.copy(), field_to_sort)
print("\nLista de libros ordenada con selección:")
print(list_selection_sort)

# Ordenamos con burbuja
list_bubble_sort = bubble_dictionary(books.copy(), field_to_sort)
print("\nLista de libros ordenada con burbuja:")
print(list_bubble_sort)