n = input()
arr = [int(item) for item in input().split()]


def merge(arr,temp_left, temp_right):
    i = j = k = 0
    while i < len(temp_left) and j < len(temp_right):
        if temp_left[i] < temp_right[j]:
            arr[k] = temp_left[i]
            i += 1
        else:
            arr[k] = temp_right[j]
            j += 1
        k += 1
    while i < len(temp_left):
        arr[k] = temp_left[i]
        i += 1
        k += 1
    while j < len(temp_right):
        arr[k] = temp_right[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


def print_result(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")


if __name__ == '__main__':
    merge_sort(arr)
    print_result(arr)
