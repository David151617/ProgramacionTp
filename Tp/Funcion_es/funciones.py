import random
def add_digits (number):
    #convierte el número en una cadena para poder acceder a sus dígitos.
    number_str = str(number)
    #Inicializa una variable para almacenar la suma de los dígitos
    add = 0
    #Itera a través de los dígitos y suma cada uno 
    for digits in number_str:
        add += int(digits)
    return add    

def choice_words (): #de la lista de palabras que tenemos nos trae una al azar
    words = {"Tecnologia", "informatica", "Elefante", "Mastodonte", "Singular", "Onomatopeya", "Cirujano", "Osteoporosis"}
    #mediante random, traemos una palabra al azar
    aleatory_word = random.choice(words)
    return aleatory_word

def bubble_sort(arr):
    # Obtén la longitud del arreglo
    n = len(arr)

    # Itera a través de todos los elementos del arreglo
    for i in range(n):
        # En cada iteración, se compara y mueve el elemento más grande hacia el final del arreglo
        # El bucle interior compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambia los elementos si el actual es mayor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# La función bubble_sort ordena el arreglo de entrada 'arr' en orden ascendente.

def quicksort(arr):
    # Verifica si el arreglo es vacío o tiene un solo elemento, en cuyo caso ya está ordenado
    if len(arr) <= 1:
        return arr
    else:
        # Selecciona el primer elemento del arreglo como el pivote
        pivot = arr[0]

        # Crea dos listas, 'lesser' (menores o iguales al pivote) y 'greater' (mayores que el pivote)
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        # Llama recursivamente a quicksort en las sublistas 'lesser' y 'greater,
        # y luego concatena las tres listas para obtener el arreglo ordenado
        return quicksort(lesser) + [pivot] + quicksort(greater)

# La función quicksort implementa el algoritmo de ordenamiento rápido (quicksort),
# que divide el arreglo en subarreglos más pequeños, ordena esos subarreglos y los combina
# para obtener el arreglo ordenado en su totalidad.


# El def merge_sort y merge trabajan como uno solo
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llamada recursiva para ordenar las dos mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combina las dos mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    # Crea una lista vacía para almacenar el resultado de la fusión
    result = []

    # Inicializa dos índices (i y j) para seguir la posición actual en las listas 'left' y 'right', respectivamente
    i = j = 0

    # Mientras haya elementos en ambas listas 'left' y 'right'
    while i < len(left) and j < len(right):
        # Compara los elementos en las posiciones 'i' y 'j' de las listas 'left' y 'right'
        if left[i] < right[j]:
            # Si el elemento en 'left' es menor, lo agrega al resultado y avanza el índice 'i'
            result.append(left[i])
            i += 1
        else:
            # Si el elemento en 'right' es menor o igual, lo agrega al resultado y avanza el índice 'j'
            result.append(right[j])
            j += 1

    # Después de salir del bucle while, es posible que todavía queden elementos en 'left' o 'right'.
    # Se añaden los elementos restantes al resultado (si los hay).
    result.extend(left[i:])
    result.extend(right[j])

    # Devuelve la lista 'result', que contiene la fusión ordenada de 'left' y 'right'
    return result

# La función merge se utiliza en el algoritmo de ordenamiento por mezcla (merge sort) para fusionar dos listas ordenadas en una sola lista ordenada.


def busqueda_lineal(arr, elemento):
    # Itera a través de los elementos del arreglo 'arr'
    for i in range(len(arr)):
        # Compara cada elemento con el 'elemento' buscado
        if arr[i] == elemento:
            # Si se encuentra el 'elemento', devuelve el índice en el que se encuentra
            return i
    # Si el 'elemento' no se encuentra en el arreglo, devuelve -1 para indicar que no se encontró
    return -1

# La función busqueda_lineal realiza una búsqueda lineal (secuencial) en un arreglo 'arr' para encontrar un 'elemento' dado.
# Devuelve el índice en el que se encuentra el 'elemento' si se encuentra, o -1 si no se encuentra.



def fill_list(i):
    # Se recibe un valor 'i' que representa la posición actual en la lista
    x = i
    
    # Se solicita al usuario que ingrese un número
    number = int(input(f"Ingrese el {i}° número "))

    # Se verifica si el número ingresado está dentro del rango permitido (entre 1 y 99)
    if number < 1 or number > 99:
        print("ERROR: el número ingresado es incorrecto. Inténtelo nuevamente.")
        # En caso de un número incorrecto, se muestra un mensaje de error y se vuelve a llamar a la función para ingresar otro número
        fill_list(x)    
    else:
        # Si el número es válido, se devuelve
        return number

# La función fill_list se utiliza para solicitar al usuario un número, verificar si está dentro del rango permitido,
# y devolver el número válido. Es probable que sea parte de un programa más grande que llenará una lista con estos números.


def full_list():
    # Crea una lista vacía llamada 'list_1' para almacenar los números ingresados por el usuario
    list_1 = []
    
    # Inicializa un contador 'i' en 1
    i = 1
    
    # Utiliza un bucle while para solicitar números al usuario y llenar la lista
    while True:
        # Llama a la función 'fill_list' para obtener un número y lo almacena en 'number'
        number = fill_list(i)
        
        # Agrega 'number' a la lista 'list_1'
        list_1.append(number)
        
        # Incrementa el contador 'i'
        i += 1
        
        # Verifica si se han ingresado 5 números (i == 6) y, en ese caso, sale del bucle while
        if i == 6:
            break
    
    # Devuelve la lista 'list_1' que contiene los números ingresados por el usuario
    return list_1

# La función full_list utiliza un bucle while para solicitar al usuario 5 números y los almacena en una lista.


def document_verify(number):
    # Define los valores mínimo y máximo de longitud permitida
    minimum = 7
    maximum = 8

    # Obtiene la longitud del número dado
    length = len(str(number))

    # Compara la longitud del número con el rango permitido
    if length < minimum or length > maximum:
        # Si la longitud no está dentro del rango, la función devuelve False
        return False
    else:
        # Si la longitud está dentro del rango, la función devuelve True
        return True


def last_word(string):
    # Elimina espacios en blanco adicionales al principio y al final de la cadena
    string = string.strip()

    # Divide la cadena en palabras utilizando espacios en blanco como delimitadores
    palabras = string.split()

    # Verifica si hay al menos una palabra en la cadena
    if len(palabras) > 0:
        # Obtiene la última palabra en la lista de palabras
        ultima_palabra = palabras[-1]

        # Devuelve la longitud de la última palabra
        return len(ultima_palabra)
    else:
        # Si no hay palabras en la cadena, devuelve 0
        return 0


def identificator(name, last_name, dni):
    # Convierte el número de documento en una cadena
    document = str(dni)

    # Obtiene el primer nombre del nombre completo y lo convierte a minúsculas
    first_name = name.split()[0].lower()

    # Calcula la longitud del apellido
    number_of_letters = len(last_name)

    # Obtiene los tres primeros dígitos del número de documento como una cadena
    three_first_number = str(document)[:3]

    # Combina los componentes para crear un identificador único
    identificator = first_name + str(number_of_letters) + three_first_number

    # Devuelve el identificador generado
    return identificator


def multiple(num1, num2):
    # Verifica si el primer número es múltiplo del segundo número
    if num1 % num2 == 0:
        # Si el residuo de la división es cero, entonces num1 es múltiplo de num2
        return True
    else:
        # Si el residuo no es cero, num1 no es múltiplo de num2
        return False

#Otros métodos de ordenamientos:
def bubble_sort(arr):
    n = len(arr)

    # Recorre todos los elementos en la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n - i - 1):
            # Intercambia si el elemento encontrado es mayor
            # que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def ascending_selection(list_1):
    # Obtener la longitud de la lista
    n = len(list_1)
    
    # Bucle externo para recorrer la lista
    for i in range(n - 1):
        # Inicializar el índice mínimo en la posición actual
        minimum_index = i
        
        # Bucle interno para encontrar el índice del elemento mínimo en la parte no ordenada
        for j in range(i + 1, n):
            # Comparar el elemento actual con el mínimo encontrado hasta ahora
            if list_1[j] < list_1[minimum_index]:
                minimum_index = j
        
        # Intercambiar el elemento actual con el mínimo encontrado
        list_1[i], list_1[minimum_index] = list_1[minimum_index], list_1[i]
    
    # Devolver la lista ordenada
    return list_1


def descending_selection(list_1):
    # Obtener la longitud de la lista
    n = len(list_1)
    
    # Bucle externo para recorrer la lista
    for i in range(n - 1):
        # Inicializar el índice máximo en la posición actual
        maximum_index = i
        
        # Bucle interno para encontrar el índice del elemento máximo en la parte no ordenada
        for j in range(i + 1, n):
            # Comparar el elemento actual con el máximo encontrado hasta ahora
            if list_1[j] > list_1[maximum_index]:
                maximum_index = j
        
        # Intercambiar el elemento actual con el máximo encontrado
        list_1[i], list_1[maximum_index] = list_1[maximum_index], list_1[i]
    
    # Devolver la lista ordenada
    return list_1


def selection_dictionary(lista, clave):
    # Obtener la longitud de la lista
    n = len(lista)

    # Bucle externo para recorrer la lista
    for i in range(n - 1):
        # Inicializar el índice mínimo en la posición actual
        indice_minimo = i

        # Bucle interno para encontrar el índice del elemento mínimo en la parte no ordenada
        for j in range(i + 1, n):
            # Comparar el valor del campo especificado en cada diccionario
            if lista[j][clave] < lista[indice_minimo][clave]:
                # Actualizar el índice mínimo si se encuentra un valor menor
                indice_minimo = j

        # Intercambiar el diccionario actual con el diccionario con el valor mínimo encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    # Devolver la lista ordenada
    return lista

def bubble_dictionary(lista, clave):
    # Obtener la longitud de la lista
    n = len(lista)

    # Bucle externo para recorrer la lista
    for i in range(n - 1):
        # Bucle interno para comparar y intercambiar elementos
        for j in range(0, n - i - 1):
            # Comparar el valor del campo especificado en cada diccionario
            if lista[j][clave] > lista[j + 1][clave]:
                # Intercambiar los diccionarios si el valor del campo es mayor
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Devolver la lista ordenada
    return lista


def insertion_sort(list_1):
    # Bucle externo para recorrer la lista desde el segundo elemento hasta el último
    for i in range(1, len(list_1)):
        # Guardar el elemento actual en una variable temporal
        current = list_1[i]
        # Inicializar el índice para comparar con el elemento actual
        j = i - 1

        # Bucle interno para mover los elementos mayores que el actual a la derecha
        while j >= 0 and current < list_1[j]:
            list_1[j + 1] = list_1[j]
            j -= 1

        # Insertar el elemento actual en la posición correcta
        list_1[j + 1] = current

    # Devolver la lista ordenada
    return list_1

def is_power(n, b):
    # Caso base: Si n es 1, entonces es una potencia de cualquier número.
    if n == 1:
        return True

    # Inicializar la potencia y realizar el bucle mientras n sea divisible por b.
    power = 1
    while power < n:
        power *= b
        if power == n:
            return True

    # Si llegamos a este punto, n no es una potencia de b.
    return False

def find_potitions(a, b, inicio=0):
    # Encontrar la primera ocurrencia de b en a a partir de la posición de inicio
    potitions = a.find(b, inicio)

    # Si no se encuentra más ninguna ocurrencia, devolver una lista vacía
    if potitions == -1:
        return []
    
    # Si se encuentra una ocurrencia, realizar la llamada recursiva para encontrar las siguientes
    potitions_rest = find_potitions(a, b, potitions + 1)

    # Devolver la posición actual y las posiciones encontradas en el resto de la cadena
    return [potitions] + potitions_rest

def pair(n):
    if n == 0:
        return True
    elif n > 0:
        return odd(n - 1)
    else:
        return False  # Consideramos que los números negativos no son ni pares ni impares.

def odd(n):
    if n == 1:
        return True
    elif n > 1:
        return pair(n - 1)
    else:
        return False  # Consideramos que los números negativos no son ni pares ni impares.

def find_greater(list_1):
    # Caso base: si la lista está vacía, no hay un mayor elemento.
    if not list_1:
        return None

    # Caso base: si la lista tiene un solo elemento, ese es el mayor.
    if len(list_1) == 1:
        return list_1[0]

    # Comparar el primer elemento con el mayor del resto de la lista.
    grater_rest = find_greater(list_1[1:])

    # Devolver el mayor entre el primer elemento y el mayor del resto.
    return list_1[0] if list_1[0] > grater_rest else grater_rest