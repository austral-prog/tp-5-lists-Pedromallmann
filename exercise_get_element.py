# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """
    if len(lista) == 0:
        return None


    if indice < 0:
        indice = len(lista) + indice

    if indice >= 0 and indice < len(lista):
        return lista[indice]

    if indice < 0 or indice >= len(lista):
        return None

print(get_element([], 1))
print(get_element([10, 20, 30], 1))
print(get_element([10, 20, 30], 2))
print(get_element([10, 20, 30], -10))
