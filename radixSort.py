import numpy as np


def radix_sort(arr):
    """
    Implementa o algoritmo de Radix Sort para ordenar um array de números inteiros.

    Args:
        arr: O array de números inteiros a ser ordenado.
    """

    # Encontra o maior número no array para determinar o número máximo de dígitos
    max_num = max(arr)

    # Itera sobre cada dígito, começando pelo dígito menos significativo
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


def counting_sort(arr, exp):
    """
    Implementa o algoritmo de Counting Sort para ordenar um array de números inteiros com base em um determinado dígito.

    Args:
        arr: O array de números inteiros a ser ordenado.
        exp: O expoente que determina o dígito a ser considerado.
    """

    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Conta a frequência de cada dígito
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Calcula as posições de cada dígito na saída
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Coloca os elementos no array de saída de acordo com suas posições
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copia os elementos ordenados de volta para o array original
    for i in range(n):
        arr[i] = output[i]


# Exemplo de uso
numeros = [170, 45, 75, 90, 802, 24, 2, 66]
print("Antes da ordenação:", numeros)

radix_sort(numeros)

print("Depois da ordenação:", numeros)
