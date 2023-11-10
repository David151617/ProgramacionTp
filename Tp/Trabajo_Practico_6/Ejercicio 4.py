'''Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado.
Imprimir esta nueva lista, iterando por ella.'''
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

print("-------")
new_number = int(input("Ingrese otro número por favor: "))
new_list = []
for i in list_of_numbers:
    if new_number > i:
        new_list.append(i)

print(f"Los números menores a {new_number} son: ")
for i in new_list:
    print(f"{i} /", end=" ")

print(" ")

frequency = {}
for i in list_of_numbers:
    frequency[i] = frequency.get(i, 0) + 1

new_list_1 = [(i, frequency[i]) for i in frequency]

print("La nueva lista es: ")
print(new_list_1)
