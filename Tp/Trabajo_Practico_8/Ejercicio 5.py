from funciones import find_greater
import random
'''Escribir una función recursiva que encuentre el mayor elemento de una lista.'''
new_list = []
number = int(input("Ingrese el número del tamaño de la lista: "))
for i in range(number): #Recorremos el tamaño indicado
    new_number = random.randint(1, 1000) #Le asignamos valores al azar
    new_list.append(new_number) 
print(f"Su lista es: {new_list}")
print("------")
result = find_greater(new_list)
print(f"El número mayor de su lista es: {result}")
