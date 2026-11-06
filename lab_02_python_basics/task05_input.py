first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")

age_text = input("Введите возраст (без преобразования): ")
print("Тип возраста без преобразования:", type(age_text))

age = int(input("Введите возраст: "))
height = float(input("Введите рост в метрах: "))

print("Имя:", first_name)
print("Фамилия:", last_name)
print("Возраст:", age, type(age))
print("Рост:", height, type(height))
