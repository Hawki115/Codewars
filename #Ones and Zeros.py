def binary_array_to_number(arr):
    total = 0
    
    for i in range(len(arr)):
        bit = arr[i]
        power = len(arr) - 1 - i
        value = bit * (2 ** power)
        total += value
    return total