def imperative(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and array[j] < item_to_insert:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item_to_insert

list = [5,4,6,3,7,2,8]
imperative(list)
print(list)