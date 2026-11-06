measurements = (12.5, 14.1, 13.8, 15.2, 12.9, 14.7, 13.3, 15.0)
print("Первый:", measurements[0])
print("Последний:", measurements[-1])
print("Срез [2:5]:", measurements[2:5])

first, second = measurements[:2]
print("Распаковка:", first, second)

as_list = list(measurements)
as_list[0] = 10.0
measurements = tuple(as_list)
print("Новый кортеж:", measurements)
