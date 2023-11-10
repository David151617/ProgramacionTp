'''Imprimir la sumatoria de todos los números de la lista.'''
print("Ingrese cuantos números desee, para finalizar ingrese el número 0(cero): ")
list_of_numbers = []
i = 1
counter = 0
while(True):
    number = int(input(f"Ingrese su {i}° número :"))
    if (number != 0):
        list_of_numbers.append(number)
        i += 1
    else :
        break
for i in list_of_numbers:
    print(f"{i} /", end=" ")
number_list_1 = len(list_of_numbers)
print("  ")
remove_of_the_list = int(input("Ingrese un número para quitar de la lista: "))
for i in list_of_numbers :
    if i == remove_of_the_list :
        list_of_numbers.remove(i)
        break
numbre_list_2 = len(list_of_numbers)
if number_list_1 == numbre_list_2:
    print("No se pudo eliminar su número ya que no pertenecía a la lista!!")
for i in list_of_numbers:
    print(f"{i} /", end=" ")

print(" ")
print("La suma de los ítems de la lista es: ")
for i in list_of_numbers:
    counter += i
print(counter)