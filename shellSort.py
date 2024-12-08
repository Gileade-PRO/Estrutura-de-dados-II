def shell_sort(arr):
    """
    Implementa o algoritmo de Shell Sort para ordenar uma lista de números.

    Args:
        arr: A lista de números a ser ordenada.
    """

    tamanho = len(arr)

    for gap in range(tamanho // 2, 0, -2):
        for i in range(gap, tamanho):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp


def imprimir_array(arr):
    """
    Imprime os elementos de uma lista em uma única linha, separados por espaços.

    Args:
        arr: A lista de números a ser impressa.
    """

    for num in arr:
        print(num, end=" ")
    print()


def executar():
    """
    Executa o algoritmo de Shell Sort com um exemplo de lista de números.
    """

    numeros = [12, 34, 54, 2, 3]
    print("Números antes da ordenação:")
    imprimir_array(numeros)

    shell_sort(numeros)

    print("Números após a ordenação:")
    imprimir_array(numeros)


if __name__ == "__main__":
    executar()