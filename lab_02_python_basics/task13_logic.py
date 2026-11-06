def check_access(age, has_access):
    print("Возраст:", age)
    print("Допуск имеется:", has_access)
    if age >= 18 and has_access:
        print("Доступ разрешён")
    else:
        print("Доступ запрещён")
    print()


check_access(19, True)
check_access(17, True)
check_access(20, False)
check_access(16, False)

# Используется and, потому что должны выполняться оба условия сразу:
# возраст от 18 лет и наличие допуска. С or доступ получил бы
# и несовершеннолетний с допуском, и взрослый без допуска.
