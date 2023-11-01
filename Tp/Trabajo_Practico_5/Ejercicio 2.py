'''
2.	Escribir una función que, dado un string, retorne la longitud de la última palabra.
Se considera que las palabras están separadas por uno o más espacios. 
También podría haber espacios al principio o al final del string pasado por parámetro.
'''
import sys
sys.path.append("C:/Users/David Amore/Desktop/Tp")
from Funcion_es import funciones

work = input("Ingrese una frase cualquiera: ") 
# Asignamos la frase a la variable para poder enviarla al método

#enviamos la palabra al método y lo qe retorne nos dara el resultado
result = funciones.last_word(work) 
print(f"La longitud de la ultima palabra es: {result} ")
