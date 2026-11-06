def check_not_empty(numbers):
    if not numbers:
        raise ValueError("Список чисел пуст")


def calculate_average(numbers):
    check_not_empty(numbers)
    return sum(numbers) / len(numbers)


def find_max(numbers):
    check_not_empty(numbers)
    maximum = numbers[0]
    for number in numbers[1:]:
        maximum = max(maximum, number)
    return maximum


def count_positive(numbers):
    return sum(1 for number in numbers if number > 0)


def analyze_numbers(numbers):
    """Возвращает минимум, максимум и среднее значение списка."""
    check_not_empty(numbers)
    minimum = maximum = numbers[0]
    for number in numbers[1:]:
        minimum = min(minimum, number)
        maximum = max(maximum, number)
    return minimum, maximum, calculate_average(numbers)
