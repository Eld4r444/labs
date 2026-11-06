def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


numbers = [4, 8, 15, 16, 23, 42, 7, 19, 31, 12]
print(find_element(numbers, 23))
print(find_element(numbers, 99))
