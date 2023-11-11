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




