from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()


"""
Bubble Sort
"""


def bubble_sort(list_of_number):
    list_len = len(list_of_number)

    for i in range(list_len - 1):
        for j in range(list_len - 1 - i):
            if list_of_number[j] > list_of_number[j + 1]:
                list_of_number[j], list_of_number[j + 1] = (
                    list_of_number[j + 1],
                    list_of_number[j],
                )

    return list_of_number


"""
Selection Sort
"""


def selection_sort(list_of_number):

    for i in range(len(list_of_number)):
        min_index = i

        for j in range(i, len(list_of_number)):
            if list_of_number[min_index] > list_of_number[j]:
                min_index = j

        list_of_number[i], list_of_number[min_index] = (
            list_of_number[min_index],
            list_of_number[i],
        )

    return list_of_number


"""
Insertion Sort
"""


def insertion_sort(list_of_number):

    for i in range(1, len(list_of_number)):

        key = list_of_number[i]
        j = i - 1

        while j >= 0 and key < list_of_number[j]:
            list_of_number[j + 1] = list_of_number[j]
            j -= 1

        list_of_number[j + 1] = key
    logger.info(list_of_number)
    return list_of_number


"""
Quick Sort
"""


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            array[i + 1], array[j] = array[j], array[i + 1]
            i += 1
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def quick_sort(array, low, high):
    # base case low < high
    if low < high:

        p = partition(array, low, high)

        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)
    return array


"""
Merge Sort
"""


def merge(array, l, m, r):
    len_1 = m - l + 1
    len_2 = r - m

    # create two arrary for two parts
    left = []
    right = []
    # copy array between two parts
    for i in range(0, len_1):
        left.append(array[l + i])

    for j in range(0, len_2):
        right.append(array[m + 1 + j])

    i = 0
    j = 0
    k = l
    # comparing two parts
    while i < len_1 or j < len_2:

        if i == len_1:  # inserting remaining part
            array[k] = right[j]
            j += 1

        elif j == len_2:  # inserting remaining part
            array[k] = left[i]
            i += 1

        elif left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        elif left[i] >= right[j]:
            array[k] = right[j]
            j += 1
        k += 1
    return array


def merge_sort(array, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        merge_sort(array, l, m)
        merge_sort(array, m + 1, r)
        merge(array, l, m, r)
    return array
