# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """

    if len(lista) >= 6:
        del lista[0]
        del lista[4-1]
        del lista[5-2]
        return lista
    elif len(lista) >= 5:
        del lista[0]
        del lista[4-1]
        return lista
    elif len(lista) != 0:
        del lista[0]
        return lista
    else:
        return lista

print(remove_elements([1,2,3,4,5,6,7,8,9,10]))
print(remove_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))
print(remove_elements([]))
print(remove_elements(['Audi', 'BMW', 'Porsche', 'Aston Martin']))
