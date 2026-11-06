def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def find_min(numbers):
    result = numbers[0]
    for number in numbers:
        if number < result:
            result = number
    return result


def find_max(numbers):
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result


numbers = [4, 8, 15, 16, 23, 42, 7, 19, 31, 12]
print("calculate_sum:", calculate_sum(numbers), "| sum:", sum(numbers))
print("find_min:", find_min(numbers), "| min:", min(numbers))
print("find_max:", find_max(numbers), "| max:", max(numbers))
