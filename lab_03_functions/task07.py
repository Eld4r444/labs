numbers = [4, 8, 15, 16, 23, 42, 7, 19, 31, 12]
print("Количество:", len(numbers))
print("Сумма:", sum(numbers))
print("Минимум:", min(numbers))
print("Максимум:", max(numbers))
print("Среднее:", sum(numbers) / len(numbers))

sorted_numbers = sorted(numbers)
print("sorted():", sorted_numbers)
print("Исходный список:", numbers)

numbers.sort()
print("После sort():", numbers)
