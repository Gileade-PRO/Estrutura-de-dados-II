import random


def exponential_search(arr, x):
    """
    Realiza uma busca exponencial em um array ordenado.

    Args:
        arr: O array ordenado.
        x: O elemento a ser procurado.

    Returns:
        O índice do elemento se encontrado, caso contrário retorna -1.
    """

    if arr[0] == x:
        return 0

    n = len(arr)
    i = 1
    while i < n and arr[i] <= x:
        i *= 2

    return binary_search(arr, int(i / 2), min(i, n - 1), x)


def binary_search(arr, l, r, x):
    """
    Realiza uma busca binária em um array ordenado.

    Args:
        arr: O array ordenado.
        l: Índice esquerdo do subarray.
        r: Índice direito do subarray.
        x: O elemento a ser procurado.

    Returns:
        O índice do elemento se encontrado, caso contrário retorna -1.
    """

    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, r, x)

    else:
        return -1


# Exemplo de uso
if __name__ == "__main__":
    numeros = [2, 3, 4, 10, 40, 50, 60, 70]
    alvo = 50

    resultado = exponential_search(numeros, alvo)

    if resultado != -1:
        print("Elemento encontrado no índice:", str(resultado))
    else:
        print("Elemento não encontrado")

    # Gerando um array aleatório grande para demonstração
    grande_array = sorted(random.sample(range(1, 1000000), 100000))
    alvo_grande = grande_array[random.randint(0, len(grande_array) - 1)]
    resultado_grande = exponential_search(grande_array, alvo_grande)
    print("Busca em um array grande:", resultado_grande)
