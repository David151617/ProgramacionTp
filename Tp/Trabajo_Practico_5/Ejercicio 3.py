'''
3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254
'''
import sys
sys.path.append("C:/Users/David Amore/Desktop/Tp")
from Funcion_es import funciones

while True:
    full_name = input("Ingrese el nombre completoo del socio(o presione Enter para finalizar): ")
    if not full_name:
        break
    dni = int(input("Ingrese el número de DNI del socio: "))
    if funciones.document_verify(dni):
        parts_name = full_name.split()
        name = parts_name[0]
        last_name = parts_name[-1]
        identificator_1 = funciones.identificator(name, last_name, dni)
        print("ID --> " + identificator_1)
    else:
        print("El número de DNI debe tener entre y u 8 dígitos. Intentelo nuevamente!!")        