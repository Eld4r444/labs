numbers = [4, 8, 15, 16, 23, 42, 7, 19, 31, 12]
print("Первый:", numbers[0])
print("Третий:", numbers[2])
print("Последний:", numbers[-1])
numbers[1] = 100
numbers.append(55)
numbers.remove(15)
print("Итоговый список:", numbers)
print("Количество элементов:", len(numbers))
