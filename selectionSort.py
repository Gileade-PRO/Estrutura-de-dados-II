def selection_sort(arr):
    """
    Implementa o algoritmo de ordenação por seleção.

    Args:
        arr: Uma lista de números a ser ordenada.
    """

    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Troca os elementos de lugar
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Array de números a ser ordenado
numeros = [64, 25, 12, 22, 11]

print("Array original:", numeros)

selection_sort(numeros)

print("Array ordenado:", numeros)
