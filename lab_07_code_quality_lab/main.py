from calculations import (
    analyze_numbers,
    calculate_average,
    count_positive,
    find_max,
)


def main():
    measurements = [10, 20, 30]
    temperatures = [-10, -5, -20]
    values = [-1, 0, 1]

    print("Среднее значение:", calculate_average(measurements))
    print("Максимальная температура:", find_max(temperatures))
    print("Положительных чисел:", count_positive(values))

    for numbers in ([3, 1, 2], [-5, -1, -3], [10, 20]):
        minimum, maximum, average = analyze_numbers(numbers)
        print(f"{numbers}: минимум {minimum}, максимум {maximum}, среднее {average}")


if __name__ == "__main__":
    main()
