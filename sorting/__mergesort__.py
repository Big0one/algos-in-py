n = input() # number of elements to be listed
arr = [int(item) for item in input().split()] # list comprehension


def merge(arr, temp_left, temp_right):
    '''
    :param arr: original list of numbers
    :param temp_left: temporary list consisting 1st half
    :param temp_right: temporary list consisting 2nd half
    :return: void
    '''
    i = j = k = 0
    # merge the temporary lists back into original list
    while i < len(temp_left) and j < len(temp_right):
        if temp_left[i] < temp_right[j]:
            arr[k] = temp_left[i]
            i += 1
        else:
            arr[k] = temp_right[j]
            j += 1
        k += 1
    # copy the remaining elements if exist
    while i < len(temp_left):
        arr[k] = temp_left[i]
        i += 1
        k += 1
    while j < len(temp_right):
        arr[k] = temp_right[j]
        j += 1
        k += 1
    return

def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        # dividing the list into two halves
        left = arr[:mid]
        right = arr[mid:]
        # sort two halves and then merge
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)
    return


def print_result(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    return


if __name__ == '__main__':
    merge_sort(arr)
    print_result(arr)
