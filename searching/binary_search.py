def binary_search_index(list_of_numbers, target_value):
    """
    :param list_of_numbers: given current increasing subsequence numbers
    :param target_value: for which position to be fixed
    :return: right position of the given value on the list of numbers
    """
    lower_index = 0                                     # set lower bound to 0 index
    higher_index = len(list_of_numbers) - 1             # set higher bound to list_length - 1

    while lower_index <= higher_index:
        mid_index = (lower_index + higher_index) // 2
        if list_of_numbers[mid_index] >= target_value:    # set > to avoid strictly increasing sub sequence
            higher_index = mid_index - 1
        else:
            lower_index = mid_index + 1

    return lower_index
