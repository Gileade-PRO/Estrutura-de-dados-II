def ternary_search(arr, left, right, key):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, key)
        elif key > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, key)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, key)

    return -1  # Element not found

def binary_search(arr, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 7

    result_ternary = ternary_search(arr, 0, len(arr) - 1, key)
    result_binary = binary_search(arr, 0, len(arr) - 1, key)

    # Print the result of Ternary Search
    print("Resultado do Ternary Search:")
    if result_ternary != -1:
        print(f"Elemento encontrado na posição {result_ternary}")
    else:
        print("Elemento não encontrado")

    # Print the result of Binary Search
    print("Resultado do Binary Search:")
    if result_binary != -1:
        print(f"Elemento encontrado na posição {result_binary}")
    else:
        print("Elemento não encontrado")