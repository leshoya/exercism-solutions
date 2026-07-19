def find(search_list, value):
    left = 0
    right = len(search_list) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if search_list[middle] == value:
            return middle
        elif value > search_list[middle]:
            left = middle + 1
        else:
            right = middle - 1
    raise ValueError("value not in array")
