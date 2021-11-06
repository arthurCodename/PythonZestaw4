def swapping(L, left, right):
    while left < right:
        simpleSwap(L, left, right)
        left = left + 1
        right = right - 1

    return L


def simpleSwap(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr


print([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(swapping([0, 1, 2, 3, 4, 5, 6, 7, 8], 2, 7))
