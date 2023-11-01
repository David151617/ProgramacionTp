'''
1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
'''
import sys
sys.path.append("C:/Users/David Amore/Desktop/Tp")
from Funcion_es import funciones

#Le asignamos un valor a la variable
number = int(input("Ingrese su número de documento: "))
#lo enviamos al método y vuelve como booleano
if funciones.document_verify(number):
    print("Bienvenido, su documento es correcto")
else:
    print("Su número es incorrecto.. Intentelo nuevamente")