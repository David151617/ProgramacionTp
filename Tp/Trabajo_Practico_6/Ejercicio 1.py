'''Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.'''
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
    