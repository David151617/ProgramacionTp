'''A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista,
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.'''
print("Ingrese cuantos números desee, para finalizar ingrese el número 0(cero): ")
list_of_numbers = []
i = 1
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