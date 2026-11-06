n = int(input("Введите количество измерений: "))

total = 0.0
for i in range(1, n + 1):
    value = float(input(f"Измерение {i}: "))
    total = total + value

print("Сумма:", total)
if n > 0:
    print("Среднее:", total / n)
else:
    print("Нет измерений для расчёта среднего")
