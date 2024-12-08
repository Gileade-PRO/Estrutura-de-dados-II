def insertion_sort(arr):
    """Implementa o algoritmo de ordenação por inserção."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucket_sort(arr):
    MAX = 0
    """Implementa o algoritmo de ordenação por baldes."""
    # Encontra o valor máximo e mínimo no array
    max_val = max(arr)
    min_val = min(arr)

    # Calcula o tamanho do balde e o número de baldes
    bucket_size = (max_val - min_val) / MAX
    num_buckets = MAX

    # Cria uma lista de baldes
    buckets = [[] for _ in range(num_buckets)]

    # Distribui os elementos nos baldes
    for num in arr:
        bucket_index = int((num - min_val) / bucket_size)
        buckets[bucket_index].append(num)

    # Ordena cada balde
    for i in range(num_buckets):
        insertion_sort(buckets[i])

    # Concatena os baldes ordenados
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


def print_array(array):
    """Imprime o array."""
    for num in array:
        print(f"{num:.2f}", end=" ")
    print()


if __name__ == "__main__":
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

    print("Array original:")
    print_array(arr)

    sorted_arr = bucket_sort(arr)

    print("\nArray ordenado:")
    print_array(sorted_arr)
