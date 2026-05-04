# Ejercicio 5: Encontrar el máximo en una lista

def find_max(lista):
    """
    Encuentra y retorna el valor máximo en una lista de números.
    Si la lista está vacía, retorna None.

    Args:
        lista: Una lista de números

    Returns:
        El valor máximo de la lista o None si está vacía
    """
    if len(lista) == 0:
        return None

    else:
        return max(lista)

print(find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_max([-9,-5, -40, -7 ]))
print(find_max([]))
