def analyze(numbers):
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    for number in numbers:
        total += number
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum, total / len(numbers)


numbers = [4, 8, 15, 16, 23, 42, 7, 19, 31, 12]
result = analyze(numbers)
print("Кортеж:", result)

minimum, maximum, average = result
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Среднее:", average)
