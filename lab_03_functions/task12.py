def calculate_average(measurements):
    total = 0
    for value in measurements:
        total += value
    return total / len(measurements)


def find_minimum(measurements):
    result = measurements[0]
    for value in measurements:
        if value < result:
            result = value
    return result


def find_maximum(measurements):
    result = measurements[0]
    for value in measurements:
        if value > result:
            result = value
    return result


def count_above_average(measurements):
    average = calculate_average(measurements)
    count = 0
    for value in measurements:
        if value > average:
            count += 1
    return count


def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1


def analyze_measurements(measurements):
    return find_minimum(measurements), find_maximum(measurements), calculate_average(measurements)


measurements = [12.5, 14.1, 13.8, 15.2, 12.9, 14.7, 13.3, 15.0, 16.4, 11.8]
target = 14.7

minimum, maximum, average = analyze_measurements(measurements)
print("Количество измерений:", len(measurements))
print("Минимум:", minimum)
print("Максимум:", maximum)
print(f"Среднее значение: {average:.2f}")
print("Выше среднего:", count_above_average(measurements))
print(f"Индекс значения {target}:", find_value(measurements, target))
