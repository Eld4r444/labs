n = int(input("Введите целое положительное число n: "))

total = 0
for i in range(1, n + 1):
    total = total + i

print("Сумма чисел от 1 до", n, "=", total)
