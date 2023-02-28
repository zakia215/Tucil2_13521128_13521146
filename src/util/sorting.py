def quickSort(arr, low, high, tuple_att_to_sort):
    if (low < high):
        pi = partition(arr, low, high, tuple_att_to_sort)
        quickSort(arr, low, pi - 1, tuple_att_to_sort)
        quickSort(arr, pi + 1, high, tuple_att_to_sort)

def partition(arr, low, high, tuple_att_to_sort):
    i = low - 1
    pivot = arr[high][tuple_att_to_sort]
    for j in range(low, high):
        if (arr[j][tuple_att_to_sort] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1