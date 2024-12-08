import math
import time
from functools import partial


def jump_search(arr, x):
    """
    Implementa a busca por salto.

    Args:
        arr: O array ordenado.
        x: O elemento a ser buscado.

    Returns:
        O índice do elemento, se encontrado. Caso contrário, -1.
    """

    n = len(arr)
    step = int(math.sqrt(n))

    # Encontre o bloco onde o elemento pode estar
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Faça uma busca linear no bloco identificado
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev
    return -1


def binary_search(arr, low, high, x):
    """
    Implementa a busca binária.

    Args:
        arr: O array ordenado.
        low: Índice inicial do intervalo de busca.
        high: Índice final do intervalo de busca.
        x: O elemento a ser buscado.

    Returns:
        O índice do elemento, se encontrado. Caso contrário, -1.
    """

    if high >= low:
        mid = low + (high - low) // 2

        # Se o elemento estiver no meio, retorne o índice
        if arr[mid] == x:
            return mid

        # Se o elemento for menor que o meio, procure na metade esquerda
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Se o elemento for maior que o meio, procure na metade direita
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


def measure_time(search_func, arr, x):
    """
    Mide o tempo de execução de uma função de busca.

    Args:
        search_func: A função de busca a ser medida.
        arr: O array a ser buscado.
        x: O elemento a ser buscado.

    Returns:
        O tempo de execução em segundos.
    """

    partial_func = partial(search_func, arr, x)

    start_time = time.time()
    partial_func()
    end_time = time.time()
    return end_time - start_time


def main():
    sizes = [1000, 10000, 100000]

    for size in sizes:
        arr = list(range(size))
        x = size - 1

        time_jump = measure_time(jump_search,arr, x)
        time_binary = measure_time(partial(binary_search,arr), 0, size - 1, x)

        print(f"Tamanho da lista: {size}")
        print(f"Tempo de busca por salto: {time_jump:.8f} segundos")
        print(f"Tempo de busca binária: {time_binary:.8f} segundos\n")


if __name__ == "__main__":
    main()
