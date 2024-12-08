def interpolation_search(arr, n, x):
    low = 0
    high = n - 1

    while low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        # Interpolation formula
        pos = low + int((high - low) / (arr[high] - arr[low]) * (x - arr[low]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1


def binary_search(arr, n, x):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def test_searches(arr, n, x):
    print(f"Procurando {x}:")

    # Interpolation Search
    result_interpolation = interpolation_search(arr, n, x)
    if result_interpolation != -1:
        print(f"Interpolation Search: encontrado indice  {result_interpolation}")
    else:
        print("Interpolation Search: nao encontrado")

    # Binary Search
    result_binary = binary_search(arr, n, x)
    if result_binary != -1:
        print(f"Binary Search: encotrado indice {result_binary}")
    else:
        print("Binary Search: nao encontrado")


# Uniformly spaced array
arr_uniform = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n_uniform = len(arr_uniform)

# Non-uniformly spaced array
arr_non_uniform = [5, 15, 40, 45, 50, 70, 90, 130, 150, 200]
n_non_uniform = len(arr_non_uniform)

# Testing with uniformly spaced array
print("=== Uniforme ===")
test_searches(arr_uniform, n_uniform, 70)
test_searches(arr_uniform, n_uniform, 35)

# Testing with non-uniformly spaced array
print("\n=== Nao uniforme ===")
test_searches(arr_non_uniform, n_non_uniform, 70)
test_searches(arr_non_uniform, n_non_uniform, 35)
