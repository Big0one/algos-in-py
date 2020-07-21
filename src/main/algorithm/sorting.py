from src.main.logger.py_logger import PyLogger

logger = PyLogger.get_configured_logger()


def bubble_sort(list_of_number):
    list_len = len(list_of_number)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if list_of_number[j] > list_of_number[j+1]:
                list_of_number[j], list_of_number[j+1] = list_of_number[j+1], list_of_number[j]
    
    return list_of_number


def selection_sort(list_of_number):
    
    for i in range(len(list_of_number)):
        min_index = i
        
        for j in range(i, len(list_of_number)):
            if list_of_number[min_index] > list_of_number[j]:
                min_index = j
                
        list_of_number[i], list_of_number[min_index] = list_of_number[min_index], list_of_number[i]
        
    return list_of_number


def insertion_sort(list_of_number):
    
    for i in range(1, len(list_of_number)):
        
        key = list_of_number[i]
        j = i - 1
        
        for j >= 0 and key < list_of_number[j]:
            list_of_number[j + 1] = list_of_number[j]
            j -= 1
            
        list_of_number[j] = key
    logger.info(list_of_number)
    return list_of_number
        