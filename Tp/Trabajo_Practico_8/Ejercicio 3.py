from funciones import find_potitions
'''Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a.'''
string_1 = input("Ingrese la primera cadena: ")
string_2 = input("Ingrese la segunda cadena: ")
result = find_potitions(string_1, string_2)
print(result)