def binary_search(array, a):
    """
  Função para realizar a busca binária em uma lista ordenada.

  Args:
    array: Lista ordenada de elementos.
    a: Elemento a ser buscado.

  Returns:
    Índice do elemento, se encontrado, caso contrário -1.
  """

    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Se x for igual ao elemento do meio, retorna o índice do meio
        if array[mid] == a:
            return mid

        # Se x for maior, ignora a metade esquerda
        elif array[mid] < a:
            low = mid + 1

        # Se x for menor, ignora a metade direita
        else:
            high = mid - 1

    # Se o elemento não for encontrado
    return -1


# Exemplo de uso
arr = [2, 3, 4, 10, 40]
x = 10

# Função de busca
result = binary_search(arr, x)

if result != -1:
    print("Elemento está presente no índice", str(result))
else:
    print("Elemento não está presente na lista")
